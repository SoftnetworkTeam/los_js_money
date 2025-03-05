# ประกาศ Function กลาง
import math
import decimal
import numpy_financial as np
from datetime import datetime, date
from calendar import monthrange

from django import forms
from django.apps import apps
from django.db import connection, models
from django.db.models import Q, ManyToManyField, DateField, DateTimeField
from django.forms.utils import ErrorDict
from querystring_parser import parser
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


def auto_slug():
    return datetime.now().strftime('%Y%m%d%H%M%S%f')


def to_dict(self):
    opts = self._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if self.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(f.value_from_object(self).values_list('pk', flat=True))
        elif isinstance(f, DateField) and not isinstance(f, DateTimeField):
            if f.value_from_object(self) is not None:
                data[f.name] = f.value_from_object(self).strftime('%d/%m/%Y')
        else:
            data[f.name] = f.value_from_object(self)
    return data


def to_list(object):
    list_data = list()
    for foo in object:
        list_data.append(to_dict(foo))
    return list_data


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'
    max_page_size = 9999


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def from_db(cls, db, field_names, values):  # เก็บข้อมูลก่อนแก้ไข old values
        instance = super().from_db(db, field_names, values)
        instance._state.adding = False
        instance._state.db = db
        instance._old_values = dict(zip(field_names, values))
        return instance

    def data_changed(self):  # เช็ค old values กับ new values
        fields = list()
        if hasattr(self, '_old_values'):
            opts = self._meta
            if not self.pk or not self._old_values:
                return fields
            for field in opts.concrete_fields + opts.many_to_many:
                if getattr(self, field.column) != self._old_values[field.column]:
                    fields.append(str(field.verbose_name))
            return fields
        return fields


class BaseListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination
    serializer_class = None
    queryset = None

    def _build_filters(self, filters, django_filters, filter_logic):
        for filter_id in filters:
            filter = filters[filter_id]
            my_filter = dict()
            if ('field' in filter) and ('operator' in filter) and ('value' in filter):
                if filter['operator'] == 'startswith' or filter['operator'] == 'endswith' or \
                        filter['operator'] == 'contains':
                    filter['operator'] = 'i' + filter['operator']
                if filter['field'] == 'status_name':
                    filter['field'] = 'status'
                if "." in filter['field']:
                    filter['field'] = filter['field'].replace('.', '__')
                    # my_filter[filter['field']] = filter['value']
                if (filter['value'] == 'true' or filter['value'] == 'false') and filter_logic == 'AND':
                    if filter['operator'] == 'eq':
                        if filter['value'] == 'true':
                            my_filter[filter['field']] = True
                        else:
                            my_filter[filter['field']] = False
                    else:
                        if filter['value'] == 'true':
                            my_filter[filter['field'] + '__' + filter['operator']] = True
                        else:
                            my_filter[filter['field'] + '__' + filter['operator']] = False
                elif (filter['value'] == 'true' or filter['value'] == 'false') and filter_logic == 'OR':
                    my_filter = dict()
                else:
                    if filter['operator'] == 'eq':
                        my_filter[filter['field']] = filter['value']
                    else:
                        my_filter[filter['field'] + '__' + filter['operator']] = filter['value']
            if my_filter:
                django_filters.append(my_filter)
        return django_filters

    def _build_sorts(self, sorts, django_sorts):
        for sort_id in sorts:
            sort = sorts[sort_id]
            if "." in sort['field']:
                sort['field'] = sort['field'].replace('.', '__')
            if ('field' in sort) and ('dir' in sort):
                if sort['dir'].lower() == 'desc':
                    django_sorts.append('-%s' % sort['field'])
                else:
                    django_sorts.append(sort['field'])
        if (len(django_sorts) == 0):
            django_sorts.append('id')
        return django_sorts

    def get_queryset(self, *args, **kwargs):
        arguments = parser.parse(self.request.GET.urlencode())
        # print(arguments)
        filter_arg = list()
        sort_arg = list()
        filter_logic = 'and'
        items = self.queryset
        first_filter = {}
        for key, value in arguments.items():
            if key not in ['take', 'skip', 'page', 'pageSize', 'sort', 'filter']:
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        first_filter[key + '__' + key2] = value2
                else:
                    first_filter[key] = value
        if first_filter:
            items = items.filter(**first_filter)
        # if "status" in arguments:
        #     items = items.filter(status=arguments['status'])
        if ("filter" in arguments) and ('filters' in arguments['filter']):
            filter_logic = arguments['filter']['logic'].upper()
            filter_arg = self._build_filters(arguments['filter']['filters'], filter_arg, filter_logic)
        if 'sort' in arguments:
            sort_arg = self._build_sorts(arguments['sort'], sort_arg)
        else:
            sort_arg = ['id']
        # filter and sort
        my_filter_qs = Q()
        for creator_filter in filter_arg:
            filters = Q(**creator_filter)
            my_filter_qs.add(filters, filter_logic)
        # print(my_filter_qs)
        if len(sort_arg) > 0:
            items = items.filter(my_filter_qs).order_by(*sort_arg)
        return items


class EnableBackwardIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.history = [None, ]
        self.i = 0

    def next(self):
        self.i += 1
        if self.i < len(self.history):
            return self.history[self.i]
        else:
            elem = next(self.iterator, None)
            if elem:
                self.history.append(elem)
            return elem

    def prev(self):
        self.i -= 1
        if self.i == 0:
            raise StopIteration
        else:
            return self.history[self.i]


# function generate เลขที่เอกสาร
def run_document(doc_date, doc_id, branch_id):
    # ปี yy, เดือน mm
    sub_date = '{}{:02d}'.format(str(doc_date.year)[2:4], doc_date.month)
    # หมวดเอกสาร
    doc_code = ''
    app_name = ''
    model_name = ''
    field_name = ''
    try:
        MasterDocument = apps.get_model(app_label='document', model_name='MasterDocument')
    except Exception as e:
        MasterDocument = False
    if MasterDocument:
        master_document = MasterDocument.objects.filter(doc_id=doc_id).first()
        if master_document:
            doc_code = master_document.doc_code
            app_name = master_document.app_name
            model_name = master_document.model_name
            field_name = master_document.field_name
    # รหัสเอกสารสาขา
    branch_doc = ''
    try:
        MasterBranch = apps.get_model(app_label='branch', model_name='MasterBranch')
    except Exception as e:
        MasterBranch = False
    if MasterBranch:
        master_branch = MasterBranch.objects.filter(id=branch_id).first()
        if master_branch:
            branch_doc = master_branch.branch_doc
    # prefix document
    pre_doc_no = branch_doc + doc_code + '-' + sub_date
    # หาเลขเอกสารล่าสุด
    try:
        MyModel = apps.get_model(app_label=app_name, model_name=model_name)
    except Exception as e:
        MyModel = False
    if MyModel:
        # last_code = MyModel.objects.filter(**{field_name: pre_doc_no}).order_by('-'+field_name).first()
        last_code = MyModel.objects.filter(Q(**{field_name + '__startswith': pre_doc_no})).values(field_name).order_by('-' + field_name).first()
    else:
        last_code = None
    # generate document no
    if not last_code:
        doc_no = pre_doc_no + '00001'
    else:
        list_last_code = dict(last_code)
        code = list_last_code[field_name]
        code_int = int(code.split(pre_doc_no)[-1])
        width = 5
        int_running = code_int + 1
        formatted = (width - len(str(int_running))) * "0" + str(int_running)
        doc_no = pre_doc_no + str(formatted)
    return doc_no


# function check หมวดเอกสารมีการตั้ง Running หรือไม่
def running(doc_id, branch_id):
    try:
        DocumentRunning = apps.get_model(app_label='document_running', model_name='DocumentRunning')
    except Exception as e:
        DocumentRunning = False
    if DocumentRunning:
        doc_code = DocumentRunning.objects.get(document__doc_id=doc_id, branch_id=branch_id)
        if doc_code:
            return doc_code.running
        else:
            return False


# function เพิ่มเดือนจากวันที่
def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, monthrange(year, month)[1])
    return date(year, month, day)


# function ปัดเศษขึ้นหลัก 10
def roundup(x):
    return (int(math.ceil(x / 10)) * 10)


# function ปัดเศษขึ้นหลัก 5
def roundup5(x):
    return (int(math.ceil(x / 5)) * 5)


def fround2(x):
    y = round(float(x) + 0.0005, 2)
    return decimal.Decimal(str(y))


def round_serm(x):
    result_x = int(x)
    float_x = x - int(x)
    if float_x >= 0.5:
        result_x = result_x + 1
    return result_x


# function หาค่างวด PMT
def pmt_installment(loan, interest_flat_rate, fee_flat_rate, period, period_installment):
    month_period = (period * period_installment)
    if month_period == 0:
        month_period = 1
    interest_rate = (interest_flat_rate + fee_flat_rate) / 100
    return roundup5(np.pmt(interest_rate / 12, month_period, -loan) * period_installment)


# function หาวันที่ต้นเดือน
def start_of_month(date_value):
    return date_value.replace(day=1)


# function หาวันที่สิ้นเดือน
def end_of_month(date_value):
    return date_value.replace(day=monthrange(date_value.year, date_value.month)[1])


# function Check Holiday date
def check_holiday(date_value, maturity):
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT dbo.Loan_CheckHoliday(%s, %s)''', [date_value, maturity])
        row_data = cursor.fetchone()
    finally:
        cursor.close()
    return row_data[0]


def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def dictfetchone(cursor):
    """
    Return one rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    row = cursor.fetchone()
    if row:
        return dict(zip(columns, row))
    else:
        return None


def get_cont_no(cont_type, contract_id):
    cont_no = ''
    try:
        if cont_type == 'E':
            contract_model = apps.get_model(app_label='effective', model_name='EffContractInfo')
        else:
            contract_model = apps.get_model(app_label='hirepurchase', model_name='ContractInfo')
    except Exception as e:
        contract_model = False
    if contract_model:
        contract = contract_model.objects.filter(id=contract_id).values('cont_no').first()
        if contract:
            cont_no = contract['cont_no']
    return cont_no


def try_convert_date(s):
    try:
        d = datetime.strptime(s, "%d/%m/%Y").date()
    except ValueError:
        d = date.today()
    return d


def get_month_name_th(month_no):
    month_name = ''
    if 1 <= month_no <= 12:
        thai_full_months = [
            "มกราคม",
            "กุมภาพันธ์",
            "มีนาคม",
            "เมษายน",
            "พฤษภาคม",
            "มิถุนายน",
            "กรกฎาคม",
            "สิงหาคม",
            "กันยายน",
            "ตุลาคม",
            "พฤศจิกายน",
            "ธันวาคม",
        ]
        month_name = thai_full_months[month_no - 1]
    return month_name


class KendoDateField(forms.DateField):
    def to_python(self, value):
        """
        Validate that the input can be converted to a date. Return a Python
        datetime.date object.
        """
        if value in self.empty_values:
            return None
        if value in ['', 'day/month/year']:
            return None
        elif 'day' in value and 'month' in value and 'year' in value:
            return None
        elif 'day' in value or 'month' in value or 'year' in value:
            raise forms.ValidationError('{} ระบุวันที่ไม่ถูกต้อง'.format(value))
        if isinstance(value, datetime):
            return value.date()
        if isinstance(value, date):
            return value
        return super().to_python(value)

    def validate(self, value):
        # Your custom validation logic goes here
        # This method is responsible for additional validation
        super().validate(value)
        # You can add more validation specific to your needs


def get_form_errors(form_list: list) -> ErrorDict:
    msg_errors = {}
    if form_list:
        for form in form_list:
            form_error = form.errors
            if isinstance(form_error, list):
                for bar in form_error:
                    msg_errors.update(bar)
            else:
                msg_errors.update(form_error)
    # print('get_form_errors', msg_errors)
    return ErrorDict(msg_errors)
