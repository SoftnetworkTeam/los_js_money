from utilis.function import BaseListAPIView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from functools import wraps
from userauth.models import UserAuth,AuthUser
from django.shortcuts import render, redirect
from decimal import Decimal, InvalidOperation
from django.urls import reverse
from django.http import  JsonResponse,HttpResponseRedirect
from theme.models import MasterBranchAP, apmast, MasterBrand, MasterModel, MasterSubModel, MasterColor, MasterInterestRate, MasterNumberOfInstallment, MasterCustomerPrename, MasterOccupation, MasterNCB, MasterProvince, MasterAmphoe, MasterTambon, MasterResidence, MasterLivingType, MasterLivingOwner, MasterBank, MasterContractDocument,InstallmentDetail,InstallmentFile,CustomerLoanDetail, CustomerAddressDetail,CustomerInfo,CustomerAddress,MasterCifDigit,CustomerIncome,Distributor,Masterbranch,\
Masterscoringinfo,Masterincomestable,Masterincomenotstable,Mastercustomerage,Mastermaritalstatus,Masterminorchildren,Mastereducationlevel,Masterbusinesstype,Mastermonthlyprofit,Masterbusinessage,Mastercontractreason,MasterNumberOfInstallment,Mastershoptypes,Masterrentalage,MasterBank,Masterbranch,MasterContractDocument,LogUserLogin,Masterbranch, MasterCompany, UserBranch
from configurations.models import Masterscoringdetail
from configurations.views import Mastercountry

from .models import customerscore

from .serializers import MasterBranchAPSerializer, apmastSerializer, MasterOfficer, MasterOfficerSerializer, MasterBrandSerializer, MasterModelSerializer, MasterSubModelSerializer, MasterColorSerializer, interestSerializer, MasterNumberOfInstallmentSerializer, MasterCustomerPrenameSerializer, MasterOccupationSerializer, MasterNCBSerializer , MasterProvinceSerializer, MasterAmphoeSerializer, MasterTambonSerializer, MasterResidenceSerializer, MasterLivingTypeSerializer, MasterLivingOwnerSerializer, MasterBankSerializer, MasterContractDocumentSerializer,HireContactSerializer ,HireContract,CustomerLoanDetailSerializer,MasterBrandSerializer,MasterbranchSerializer
from theme.serializers import InstallmentFileSerializers

from rest_framework.pagination import PageNumberPagination
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.db import transaction, DatabaseError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import os
import time
import re

def check_permission(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user_auth = UserAuth.objects.filter(user=user, auth__auth_code='A002').first()
            if user_auth and not user_auth.status:
                return redirect('dashboard')

        return view_func(request, *args, **kwargs)

    return _wrapped_view

@login_required(login_url='/user_login')
def nameList(request):
    customer_loan_detail = CustomerLoanDetail.objects.all()
    return render(request, 'nameList.html', {'customer_loan_detail': customer_loan_detail})

@login_required(login_url='/user_login')
def detail(request, id):
    installment_obj = InstallmentDetail.objects.filter(id=id).first()
    installment_id = CustomerLoanDetail.objects.filter(id=id).first()
    customerid = installment_id.customer_id
    customer_score = customerscore.objects.filter(installmentdetail_id=id).first()
    date_now = datetime.now()
    customer_info = CustomerInfo.objects.filter(id=customerid).first()
    
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        status = request.POST.get('status')
        issue_cancel = request.POST.get('issue_cancel', '')
        score_name = request.POST.get('score_name', '').strip()
        score_set = request.POST.get('score_set')
        score_1 = request.POST.get('score_1')
        score_2 = request.POST.get('score_2')
        score_3 = request.POST.get('score_3')
        grade = request.POST.get('grade')
        
        scoring_info = Masterscoringinfo.objects.filter(id=score_set).first()
        
        if customer_info.occupation_id == 1 :
            minimum_score = scoring_info.stable_min
            minimum_dept_income = scoring_info.stable_percent
        else :
            minimum_score = scoring_info.not_stable_min
            minimum_dept_income = scoring_info.not_stable_percent
        
        current_date = datetime.now()
        installment_detail = InstallmentDetail.objects.get(id=id)
        installment_detail.status_approve = status
        installment_detail.approve_date = current_date
        installment_detail.user_approve = request.session['username']
        installment_detail.user_id = request.session['username']
        installment_detail.issue_cancel = issue_cancel
        installment_detail.save()
         
        if status == '0' or status == '1' or status == '9':
            if customer_score :
                 customerscore.objects.filter(id=customer_score.id).update(
                        score_name=score_name,
                        score_1=score_1,
                        score_2=score_2,
                        score_3=score_3,
                        grade=grade,
                        status_approve=status,
                        minimum_score=minimum_score,
                        minimum_dept_income=minimum_dept_income,
                        updated_at=date_now,
                        user_id=request.session['user_id']
                    )
            else :
                 customerscore.objects.create(
                        installmentdetail_id=id,
                        score_name=score_name,
                        score_1=score_1,
                        score_2=score_2,
                        score_3=score_3,
                        grade=grade,
                        status_approve=status,
                        minimum_score=minimum_score,
                        minimum_dept_income=minimum_dept_income,
                        created_at=date_now,
                        updated_at=date_now,
                        user_id=request.session['user_id']
                    )

        return JsonResponse({'success': True, 'message': 'บันทึกข้อมูลสำเร็จ', 'detail': issue_cancel, 'status_approve': status})

    customer_loan_detail = CustomerLoanDetail.objects.filter(id=id).first()
    prename = MasterCustomerPrename.objects.filter(id=customer_info.pre_name_id).first()
    installment = InstallmentDetail.objects.get(id=id)
    customer_range_age = Mastercustomerage.objects.filter(id=customer_info.customer_age_id).first()
    marital_status = Mastermaritalstatus.objects.filter(id=customer_info.marital_status).first()
    minorchildren = Masterminorchildren.objects.filter(id=customer_info.minorchildren_id).first()
    education = Mastereducationlevel.objects.filter(id=customer_info.education_level_id).first()
    occupation = MasterOccupation.objects.filter(id=customer_info.occupation_id).first()
    business_type = Masterbusinesstype.objects.filter(id=customer_info.business_type_id).first()
    monthly_profit = Mastermonthlyprofit .objects.filter(id=customer_info.monthlyprofit_id).first()
    business_age = Masterbusinessage.objects.filter(id=customer_info.businessage_id).first()
    contract_reason = Mastercontractreason.objects.filter(id=customer_info.contract_reason_id).first()
    number_Installment = MasterNumberOfInstallment.objects.filter(id=installment.installment).first()
    shop_type = Mastershoptypes.objects.filter(id=customer_info.shop_type_id).first()
    rentalage = Masterrentalage.objects.filter(id=customer_info.rentalage_id).first()
    customer_address_detail = CustomerAddressDetail.objects.filter(customer_id=customerid, address_id=1).first()
    customer_address2_detail = CustomerAddressDetail.objects.filter(customer_id=customerid, address_id=2).first()
    customer_address3_detail = CustomerAddressDetail.objects.filter(customer_id=customerid, address_id=3).first()
    customer = CustomerLoanDetail.objects.filter(id=id).first()

    file = InstallmentFile.objects.filter(installment_id=installment_obj.id)
    

    badge_status = ""
    loan_status = ""
    if customer_loan_detail.status_approve == 1:
        badge_status = 'success' 
        loan_status = 'Approve'
    elif customer_loan_detail.status_approve == 2:
        badge_status = 'info'
        loan_status = 'Created Contract'
    elif customer_loan_detail.status_approve == 5:
        badge_status = 'danger' 
        loan_status = 'Cancel'
    elif customer_loan_detail.status_approve == 9:
        badge_status = 'danger' 
        loan_status = 'Reject'
    else: 
        badge_status = 'warning' 
        loan_status = 'Waiting'
        
    return render(request, 'detail.html', {
        'installment_detail': installment ,
        'business_type': business_type,
        'customer_info': customer_info ,
        'prename': prename,
        'customer_range_age':customer_range_age,
        'marital_status': marital_status,
        'minorchildren': minorchildren,
        'education': education,
        'occupation': occupation,
        'monthly_profit': monthly_profit,
        'business_age': business_age,
        'contract_reason': contract_reason,
        'number_Installment': number_Installment,
        'shop_type': shop_type,
        'rentalage': rentalage,
        'customer_address_detail': customer_address_detail,
        'customer_address2_detail': customer_address2_detail,
        'customer_address3_detail': customer_address3_detail,
        "id": id,
        'file': file,
        'customer': customer,
        'badge_status': badge_status ,
        'loan_status': loan_status,
        'customer_score': customer_score
    })

def format_date_time(date_time):
    if date_time is not None:
        return date_time.strftime('%d/%m/%Y')
    else:
        return None

@login_required(login_url='/user_login')
@check_permission
def editFormcommon(request,id):
    installment = InstallmentDetail.objects.filter(id=id).first()   
    customerid = installment.customer_id
    if request.method == 'POST':    
        if request.POST['type'] == 'file':
            file = InstallmentFile.objects.filter(id=request.POST['file_id'])
            file.delete()
        else:
            current_date = datetime.now()
            customer_loan_detail_id = request.POST['id']

        return HttpResponseRedirect(reverse('edit', args=[id]))
    else:
        customer_info = CustomerInfo.objects.filter(id=customerid).first()
        prename = MasterCustomerPrename.objects.filter(id=customer_info.pre_name_id).first()
        customer_range_age = Mastercustomerage.objects.filter(id=customer_info.customer_age_id).first()
        marital_status = Mastermaritalstatus.objects.filter(id=customer_info.marital_status).first()
        minorchildren = Masterminorchildren.objects.filter(id=customer_info.minorchildren_id).first()
        education = Mastereducationlevel.objects.filter(id=customer_info.education_level_id).first()
        occupation = MasterOccupation.objects.filter(id=customer_info.occupation_id).first()
        business_type = Masterbusinesstype.objects.filter(id=customer_info.business_type_id).first()
        monthly_profit = Mastermonthlyprofit .objects.filter(id=customer_info.monthlyprofit_id).first()
        business_age = Masterbusinessage.objects.filter(id=customer_info.businessage_id).first()
        contract_reason = Mastercontractreason.objects.filter(id=customer_info.contract_reason_id).first()
        number_Installment = MasterNumberOfInstallment.objects.filter(id=installment.installment).first()
        shop_type = Mastershoptypes.objects.filter(id=customer_info.shop_type_id).first()
        rentalage = Masterrentalage.objects.filter(id=customer_info.rentalage_id).first()
        customer_address_detail = CustomerAddressDetail.objects.filter(customer_id=customerid, address_id=1).first()
        customer_address2_detail = CustomerAddressDetail.objects.filter(customer_id=customerid, address_id=2).first()
        customer_address3_detail = CustomerAddressDetail.objects.filter(customer_id=customerid, address_id=3).first()
        customer = CustomerLoanDetail.objects.filter(id=id).first()
        formatted_date_time_birth_date = format_date_time(customer_info.birth_date)
        formatted_date_time_issue_date = format_date_time(customer_info.issue_date)
        formatted_date_time_expire_date = format_date_time(customer_info.expire_date)
        formatted_date_time_date_read_card = format_date_time(installment.date_read_card)
        formatted_date_time_start_payment = format_date_time(installment.start_payment)
        
        country = Mastercountry.objects.filter(id=customer_info.country_id).first()
        bank = MasterBank.objects.filter(id=installment.bank_id).first()
        province_branch = MasterProvince.objects.filter(id=installment.create_to_province_id).first()
        branch = Masterbranch.objects.filter(id=installment.create_to_branch_id).first()
        
        file_objects = InstallmentFile.objects.filter(installment_id=installment.id).select_related('doc')

        # for file_type in file_objects:
        #     print(vars(file_type) )
    
    return render(request, 'form_common.html', { 
        'installment_detail': installment ,
        'business_type': business_type,
        'customer_info': customer_info ,
        'prename': prename,
        'customer_range_age':customer_range_age,
        'marital_status': marital_status,
        'minorchildren': minorchildren,
        'education': education,
        'occupation': occupation,
        'monthly_profit': monthly_profit,
        'business_age': business_age,
        'contract_reason': contract_reason,
        'number_Installment': number_Installment,
        'shop_type': shop_type,
        'rentalage': rentalage,
        'customer_address_detail': customer_address_detail,
        'customer_address2_detail': customer_address2_detail,
        'customer_address3_detail': customer_address3_detail,
        "id": id,
        'file': file_objects,
        'formatted_date_time_issue_date' : formatted_date_time_issue_date,
        'formatted_date_time_expire_date' : formatted_date_time_expire_date,
        'formatted_date_time_date_read_card' : formatted_date_time_date_read_card,
        'formatted_date_time_start_payment' : formatted_date_time_start_payment,
        'formatted_date_time_birth_date' : formatted_date_time_birth_date,
        'country' : country,
        'bank' : bank,
        'province_branch' : province_branch,
        'branch' : branch,
        'customer': customer,       "married_status_options": [
            {
                "id": "1",
                "text": "โสด",
                "value": "1"
            },
            {
                "id": "2",
                "text": "สมรส",
                "value": "2"
            },
            {
                "id": "3",
                "text": "หย่าร้าง",
                "value": "3"
            },
            {
                "id": "4",
                "text": "หม้าย",
            }
        ],
    }) 

@login_required(login_url='/user_login')
@check_permission
def createCustomer(request):
    return render(request, 'form_common.html', {
                "guarantee_type_options": ["เดือน", "ปี"] ,
                "married_status_options": [
                    {
                        "id": "1",
                        "text": "โสด",
                        "value": "1"
                    },
                    {
                        "id": "2",
                        "text": "สมรส",
                        "value": "2"
                    },
                    {
                        "id": "3",
                        "text": "หย่าร้าง",
                        "value": "3"
                    },
                    {
                        "id": "4",
                        "text": "หม้าย",
                        "value": "4",
                    }
                ],
                
        })
    
def check_card_no(request):
    card_no = request.GET.get('card_no', '')
    
    customer_info = CustomerInfo.objects.filter(card_no=card_no).first()
    print('customer_info:',customer_info)

    if InstallmentDetail.objects.filter(
        customer_id=customer_info.id, 
        status_approve__in=[None, 0]
    ).exists():
        return JsonResponse({"status": "success", "message": "บุคคลผู้นี้เคยขอสินเชื่อแล้ว"})
    
    return JsonResponse({"status": "error"})
    
def safe_decimal(value, default=Decimal('0')):
    try:
        # Try to remove commas and convert to Decimal
        return Decimal(value.replace(",", ""))
    except (InvalidOperation, AttributeError):
        # If conversion fails, return the default value
        return default

class CustomerLoanDetailApiView(BaseListAPIView):
    serializer_class = CustomerLoanDetailSerializer

    def get_queryset(self):
        status = self.kwargs.get('status')
        company_id = self.request.session.get('company_id')
        create_to_branch_id = self.request.session.get('branch_id')

        
        
        if(status == 'approve') :
            customer_detail = CustomerLoanDetail.objects.filter(company_id=company_id,status_approve=1)
        elif(status == 'waiting') :
            customer_detail = CustomerLoanDetail.objects.filter(company_id=company_id,status_approve__isnull=True)
        else :
            customer_detail = CustomerLoanDetail.objects.filter(company_id=company_id)

        for detail in customer_detail:
            print('branch_name sss:', detail.branch)
        
        return customer_detail


class NoLimitPagination(PageNumberPagination):
    page_size = 1000  
    
class HireContractApiView(BaseListAPIView):
    queryset = HireContract.objects.all()
    serializer_class = HireContactSerializer

class apmastAPIView(BaseListAPIView):

    def get(self, request, *args, **kwargs):
        queryset = apmast.objects.all()
        serializer = apmastSerializer(queryset, many=True)
        
        return JsonResponse({
            "results": serializer.data,
            "count": queryset.count()  
        })


class MasterBranchAPAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    queryset = MasterBranchAP.objects.all()
    serializer_class = MasterBranchAPSerializer

        
class MasterOfficerAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    queryset = MasterOfficer.objects.all()
    serializer_class = MasterOfficerSerializer

    
class MasterBrandAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterBrandSerializer

    def get_queryset(self):
        queryset = MasterBrand.objects.all()
        
        # ฟิลเตอร์ตาม brand_id ถ้ามีใน URL
        id = self.request.query_params.get('id',None)
        brand_id = self.request.query_params.get('brand_id',None)
        if brand_id:
            queryset = queryset.filter(id=brand_id)
        elif id:
            queryset = queryset.filter(id=id)
        return queryset
    
class MasterModelAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    queryset = MasterModel.objects.all()
    serializer_class = MasterModelSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id',None)
        brand_id = self.request.GET.get('brand_id',None)
        if brand_id:
            queryset = queryset.filter(brand_id=brand_id) 
        elif id:
            queryset = queryset.filter(id=id)
        return queryset


class MasterSubModelAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination

    def get(self, request, *args, **kwargs):
        # รับ id ของผู้จำหน่ายที่เลือก
        id = self.request.query_params.get('id',None)
        model_id = request.GET.get('model_id', None)
        # กรองสาขาตามผู้จำหน่ายที่เลือก (ถ้ามี apmast_id)
        if model_id:
            queryset = MasterSubModel.objects.filter(model_id=model_id)
        elif id:
            queryset = MasterSubModel.objects.filter(id=id)
        else:
            queryset = MasterSubModel.objects.none()  # ถ้าไม่มี apmast_id ก็ไม่ให้ผลลัพธ์ใดๆ
        
        serializer = MasterSubModelSerializer(queryset, many=True)
        
        return JsonResponse({
            "results": serializer.data,
            "count": queryset.count()  # นับจำนวนสาขาที่กรอง
        })

        
class MasterColorAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterColorSerializer
    
    def get_queryset(self):
        id = self.request.query_params.get('id', None)  # ใช้ query_params
        queryset = MasterColor.objects.all()  # ใช้ queryset ตรง ๆ แทน super().get_queryset()
        
        if id:
            queryset = queryset.filter(id=id)
        
        return queryset

class interestAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    queryset = MasterInterestRate.objects.all()
    serializer_class = interestSerializer


class MasterNumberOfInstallmentAPIView(BaseListAPIView):
    serializer_class = MasterNumberOfInstallmentSerializer
    
    def get_queryset(self):
        queryset = MasterNumberOfInstallment.objects.filter(status='A')
        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(installment_amount__icontains=query_param))
            
        return queryset

    
class MasterCustomerPrenameAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterCustomerPrenameSerializer

    def get_queryset(self):
        queryset = MasterCustomerPrename.objects.filter(status='A').order_by('id')

        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(pre_name__icontains=query_param))

        return queryset


class MasterOccupationAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterOccupationSerializer
    
    def get_queryset(self):
        queryset = MasterOccupation.objects.filter(status='A')

        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(occup_name__icontains=query_param))

        return queryset

class MasterProvinceAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterProvinceSerializer

    def get_queryset(self):
        queryset = MasterProvince.objects.all()
        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(province_name__icontains=query_param))

        return queryset


class MasterAmphoeAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterAmphoeSerializer        
    
    def get_queryset(self):
        province_id = self.request.GET.get('province_id', None)
        queryset = MasterAmphoe.objects.filter(province_id=province_id)
        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(amphoe_name__icontains=query_param))
        return queryset


class MasterTambonAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterTambonSerializer

    def get_queryset(self):
        amphoe_id = self.request.GET.get('amphoe_id', None)
        queryset = MasterTambon.objects.filter(amphoe_id=amphoe_id)
        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(tambon_name=query_param))
        return queryset

        
class MasterResidenceAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterResidenceSerializer
    queryset = MasterResidence.objects.filter(status='A')
   

class MasterLivingOwnerAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterLivingOwnerSerializer
    
    def get_queryset(self):
        scoring_detail = Masterscoringdetail.objects.filter(score_id='1', score_type='H')
        
        type_id= scoring_detail.values_list('type_id', flat=True)
        
        queryset = MasterLivingOwner.objects.filter(id__in=type_id,status='A')
        
        return queryset


class MasterLivingTypeAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    queryset = MasterLivingType.objects.filter(status='A').order_by('id')
    serializer_class = MasterLivingTypeSerializer
    
class MasterBankAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    queryset = MasterBank.objects.filter(status='A').order_by('id')
    serializer_class = MasterBankSerializer
    
class MasterContractDocumentAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    queryset = MasterContractDocument.objects.filter(status='A').order_by('id')
    serializer_class = MasterContractDocumentSerializer
    
    

def MasterAddress(province_name: str, amphoe_name: str, tambon_name: str):
    province = MasterProvince.objects.filter(province_name=province_name).first()
    amphoe = MasterAmphoe.objects.filter(amphoe_name=amphoe_name, province_id=province.id).first()
    tambon = MasterTambon.objects.filter(tambon_name=tambon_name, amphoe_id=amphoe.id).first()


    return str(province.id) + '##' + str(amphoe.id) + '##' + str(tambon.id)

class branchAPAPIView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterbranchSerializer
    
    def get_queryset(self):
        queryset = Masterbranch.objects.all()
        
        # ฟิลเตอร์ตาม brand_id ถ้ามีใน URL
        province_id = self.request.query_params.get('province_id',None)
        if province_id:
            queryset = queryset.filter(province_id=province_id)

        return queryset

def running_cif(first_name: str):
    # หาอักษรตัวแรก
    sub_text = first_name.strip()[0:2]
    sub_text = re.sub(r'[เ-ไ]', '', sub_text)
    sub_text = re.sub(r'[ะ-ไ]', '', sub_text)
    sub_text = re.sub(r'[่้๊๋์็]', '', sub_text)
    cif_char = sub_text[0:1]
    # เช็คว่าเป็น A - z หรือไม่
    pattern = re.compile("[A-Za-z]")
    if pattern.fullmatch(cif_char) is not None:
        master_cif_digit = MasterCifDigit.objects.filter(cif_char='A-z').values('cif_digit').first()
    else:
        master_cif_digit = MasterCifDigit.objects.filter(cif_char__contains=cif_char).values('cif_digit').first()
    if master_cif_digit:
        search_digit = master_cif_digit['cif_digit']
    else:
        search_digit = '00'
    # cust_code_count = CustomerInfo.objects.filter(cust_code__startswith=search_digit).count()
    customer_info = CustomerInfo.objects.filter(cust_code__startswith=search_digit,conversion_id__isnull=True).order_by('-cust_code').first()
    if customer_info:
        if len(customer_info.cust_code) <= 8:
            cust_code_count = int(customer_info.cust_code[2:8])
        else:
            cust_code_count = 0
    else:
        cust_code_count = 0
    zero_width = 6
    int_running = cust_code_count + 1
    formatted = (zero_width - len(str(int_running))) * "0" + str(int_running)
    new_cust_code = search_digit + str(formatted)
    return new_cust_code

def running_app(formatted_current_date: str):
    latest_installment = InstallmentDetail.objects.filter(app_id__startswith=formatted_current_date).order_by('-id').first()
    if latest_installment:
        latest_app_id = latest_installment.app_id
        running_no = latest_app_id[-4:]
        new_running_no = str(int(running_no) + 1).zfill(4)
        app_id = latest_app_id[:-4] + new_running_no
    else:
        app_id = formatted_current_date + '0001'

    return app_id

def formatDate(date_str):
    if date_str:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
        return formatted_date

def auto_slug():
    return datetime.now().strftime('%Y%m%d%H%M%S%f')

class CalScoring(BaseListAPIView):
    def post(self, request, *args, **kwargs):
        post_data = request.POST.dict()
        
        score_set = post_data.get('score_set', None) 
        occupation = post_data.get('occupation', None) #A ประเภทอาชีพ
        education = post_data.get('education', None) #C ระดับการศึกษา
        minorchildren = post_data.get('minorchildren', None) #D บุตรที่ยังไม่บรรลุนิติภาวะ
        reason = post_data.get('reason', None) #F วัตถุประสงค์
        residence = post_data.get('residence', None) #G ประเภทที่พักอาศัย
        living_type = post_data.get('living_type', None) #H สถานะที่พักอาศัย
        customer_age = post_data.get('customer_age', None) #J อายุผู้สมัคร
        shop_type = post_data.get('shop_type', None) #K ประเภทร้าน
        rentalage = post_data.get('rentalage', None) #L อายุเช่าพื้นที่
        business_type = post_data.get('business_type', None) #M ลักษณะธุรกิจ
        profit = post_data.get('profit', None) #N กำไรต่อเดือน
        business_age = post_data.get('business_age', None) #O อายุธุรกิจ
        
        category_occupation = post_data.get('category_occupation', None) #หมวดหมู่อาชีพ 1 = รายได้ประจำ , 2 = รายได้ไม่สม่ำเสมอ

        # ฟังก์ชันช่วยดึงคะแนนจาก queryset และป้องกัน None
        def get_score(obj):
            return getattr(obj, 'score', 0) if obj is not None else 0  # ถ้ามีข้อมูล ให้ดึงค่า score_value, ถ้าไม่มีให้ใช้ 0

        score_reason = Masterscoringdetail.objects.filter(score_id=score_set, score_type='F', type_id=reason).first()
        
        # คะแนน 1
        score_customer_age = get_score(Masterscoringdetail.objects.filter(score_id=score_set, score_type='J', type_id=customer_age).first())
        score_education = get_score(Masterscoringdetail.objects.filter(score_id=score_set, score_type='C', type_id=education).first())
        score_residence = get_score(Masterscoringdetail.objects.filter(score_id=score_set, score_type='G', type_id=residence).first())
        score_living_type = get_score(Masterscoringdetail.objects.filter(score_id=score_set, score_type='H', type_id=living_type).first())
        score_minorchildren = get_score(Masterscoringdetail.objects.filter(score_id=score_set, score_type='D', type_id=minorchildren).first())
        
        # grade = Masterincomestable.objects.filter(id=2).first()

        score_1 = score_customer_age + score_education + score_residence + score_living_type + score_minorchildren
        
        # คะแนน 2
        score_occupation = get_score(Masterscoringdetail.objects.filter(score_id=score_set, score_type='A', type_id=occupation).first())
        score_business_type = get_score(Masterscoringdetail.objects.filter(score_id=score_set, score_type='J', type_id=business_type).first())
        score_shop_type = get_score(Masterscoringdetail.objects.filter(score_id=score_set, score_type='K', type_id=shop_type).first())
        score_rentalage = get_score(Masterscoringdetail.objects.filter(score_id=score_set, score_type='L', type_id=rentalage).first())
        score_profit = get_score(Masterscoringdetail.objects.filter(score_id=score_set, score_type='J', type_id=profit).first())
        score_business_age = get_score(Masterscoringdetail.objects.filter(score_id=score_set, score_type='O', type_id=business_age).first())

        score_2 = score_occupation + score_business_type + score_shop_type + score_rentalage + score_profit + score_business_age
        score_3 = score_1 + score_2
        
        scoring_info = Masterscoringinfo.objects.filter(id=score_set).first()
        
        #หา type_id ของเกรด
        grade_master = Masterscoringdetail.objects.filter(
            score_id=score_set,
            score_type='Y',
            score__lte=score_3
        ).order_by('-score').first()

        if grade_master:  # ตรวจสอบว่า grade_master ไม่เป็น None
            grade_master_type_id = grade_master.type_id
        else:
            grade_master_type_id = None  # หรือกำหนดค่า default ที่เหมาะสม
         
        # __gt (greater than) ใช้สำหรับกรองค่าที่ "มากกว่า"
        # __lt (less than) ใช้สำหรับกรองค่าที่ "น้อยกว่า"
        # __gte (greater than or equal) ใช้สำหรับกรองค่าที่ "มากกว่าหรือเท่ากับ"
        # __lte (less than or equal) ใช้สำหรับกรองค่าที่ "น้อยกว่าหรือเท่ากับ"


        if category_occupation == 1: #เกณฑ์ผู้มีรายได้รายได้ประจำ
            set_stable_min = scoring_info.stable_min #คะแนนขั้นต่ำ
            set_percent = scoring_info.stable_percent #หนี้ต่อรายได้ขั้นต่ำ
            grade = Masterincomestable.objects.filter(id=grade_master_type_id).first() if grade_master_type_id else None
            if score_3 != 0.00 and set_stable_min != 0.00 and score_3 >= set_stable_min and grade_master_type_id is not None:
                message = 'แนะนำให้อนุมัติ'
            else:
                message = 'แนะนำไม่ให้อนุมัติ'
 
             
            
        else : #เกณฑ์ผู้มีรายได้ไม่สม่ำเสมอ
            set_stable_min = scoring_info.not_stable_min #คะแนนขั้นต่ำ
            set_percent = scoring_info.not_stable_percent #หนี้ต่อรายได้ขั้นต่ำ
            grade = Masterincomenotstable.objects.filter(id=grade_master_type_id).first() if grade_master_type_id else None
            if score_3 != 0.00 and set_stable_min != 0.00 and score_3 >= set_stable_min and grade_master_type_id is not None:
                message = 'แนะนำให้อนุมัติ'
            else:
                message = 'แนะนำไม่ให้อนุมัติ'

        response_data = {
            'status': 'success',
            'score_1': score_1,
            'score_2': score_2,
            'score_3': score_3,
            'message': message,
            'set_percent_': set_percent ,
            'grade': grade.grade_code if grade and score_3 != 0.00 else 'N/A',

        }
        return JsonResponse(response_data)


def insertInstallment(request):
    if request.method == 'POST':
        
        # return JsonResponse({"status": "success", "message": "Received data", "data": request.POST}, status=200)
        id = request.POST.get('id', None)
        post_data = request.POST.dict()

        if post_data['send_doc'] == 'card':
            card_send_doc = 'Y'
        else:
            card_send_doc = 'N'

        if post_data['send_doc'] == 'current':
            current_send_doc = 'Y'
        else:
            current_send_doc = 'N'

        if post_data['send_doc'] == 'company':
            company_send_doc = 'Y'
        else:
            company_send_doc = 'N'

        current_date = datetime.now()
        formatted_current_date = current_date.strftime("APP-%Y%m")
        if not id:
            app_id = running_app(formatted_current_date)
        # ข้อมูลลูกค้า
        try:
            with (transaction.atomic()):
                try:
                    prenamefilter = MasterCustomerPrename.objects.filter(pre_name=post_data['prename']).first()
                except MasterCustomerPrename.DoesNotExist:
                    prenamefilter = None

                if prenamefilter:
                    prename = post_data['prename']
                else:
                    prenamecreate = MasterCustomerPrename.objects.create(
                        pre_name=post_data['prename'],
                        status="A",
                        slug=auto_slug(),
                    )
                    prenamecreate.save()

                try:
                    customerInfo = CustomerInfo.objects.filter(card_no=post_data['card_id']).first()
                except CustomerInfo.DoesNotExist:
                    customerInfo = None

                if customerInfo:
                    first_name = post_data['first_name']
                    last_name = post_data['last_name']
                    address_diffshift = post_data.get('address_diffshift', '')
                    
                    if address_diffshift == 'true':
                        prename = MasterCustomerPrename.objects.filter(pre_name=post_data['prename'], status='A').first()
                        prename_id = prename.id
                    else :
                        prename_id = post_data['prename']

                        
                    customerInfo.first_name = first_name
                    customerInfo.last_name = last_name
                    customerInfo.gender = post_data['gender']
                    customerInfo.birth_date = formatDate(post_data['birthday'])
                    customerInfo.customer_age_id = post_data['customer_age']
                    customerInfo.issue_date = formatDate(post_data['issue_date'])
                    customerInfo.expire_date = formatDate(post_data['expire_date'])
                    customerInfo.mobile = post_data['mobile']
                    customerInfo.telephone = post_data['telephone']
                    customerInfo.minorchildren_id = post_data['minorchildren']
                    customerInfo.education_level_id = post_data['education_level_id']
                    
                    customerInfo.email = post_data['email']
                    customerInfo.line_id = post_data['line_id']
                    customerInfo.marital_status = post_data['married_status']
                    customerInfo.occupation_id = post_data['occup']
                    customerInfo.category_occupation = post_data['category_occupation']
                    customerInfo.business_type_id = post_data['business_type_id']
                    customerInfo.shop_type_id = post_data['shop_type_id']
                    customerInfo.rentalage_id = post_data['rentalage_id']
                    customerInfo.monthlyprofit_id = post_data['monthlyprofit_id']
                    customerInfo.businessage_id = post_data['businessage_id']
                    customerInfo.contract_reason_id = post_data['contract_reason']
                    customerInfo.age = post_data['age']
                    customerInfo.book_no =  post_data.get('book_no', None) 
                    customerInfo.book_name = post_data.get('book_name', None)
                    customerInfo.bank_id = post_data.get('bank_id', None)
                    customerInfo.guarantor_name = post_data.get('guarantor_name', '')
                    customerInfo.country_id = post_data['country_id']
                    customerInfo.channel_payment = post_data['channel_payment']
                    customerInfo.memo = post_data['telephone']
                    customerInfo.pre_name_id = prename_id
                    customerInfo.updated_at = current_date
                    customerInfo.refer_name = post_data['refer_name']
                    customerInfo.refer_description = post_data['refer_description']
                    customerInfo.refer_telephone = post_data['refer_telephone']
                    customerInfo.save()
                else:
                    first_name = post_data['first_name']
                    last_name = post_data['last_name']
                    new_cust_code = running_cif(first_name)
                    address_diffshift = post_data.get('address_diffshift', '')
                    
                    if address_diffshift == 'true':
                        prename = MasterCustomerPrename.objects.filter(pre_name=post_data['prename'], status='A').first()
                        prename_id = prename.id
                    else :
                        prename_id = post_data['prename']

                    customerInfo = CustomerInfo.objects.create(
                        cust_type='I',
                        cust_code=new_cust_code,
                        first_name=first_name,
                        last_name=last_name,
                        gender=post_data['gender'],
                        card_type=1,
                        card_no=post_data['card_id'],
                        birth_date=formatDate(post_data['birthday']),
                        customer_age_id=post_data['customer_age'],
                        issue_date=formatDate(post_data['issue_date']),
                        expire_date=formatDate(post_data['expire_date']),
                        telephone=post_data['telephone'],
                        minorchildren_id=post_data['minorchildren'],
                        education_level_id=post_data['education_level_id'],
                        email=post_data['email'],
                        line_id=post_data['line_id'],
                        category_occupation=post_data.get('category_occupation', ''), 
                        business_type_id=post_data['business_type_id'],
                        shop_type_id=post_data['shop_type_id'],
                        rentalage_id=post_data['rentalage_id'],
                        monthlyprofit_id=post_data['monthlyprofit_id'],
                        businessage_id=post_data['businessage_id'],
                        age=post_data['age'],
                        book_no=post_data.get('book_no', None) ,  
                        book_name=post_data.get('book_name', None) , 
                        guarantor_name=post_data.get('guarantor_name', ''), 
                        country_id=post_data['country_id'],
                        contract_reason_id=post_data['contract_reason'],
                        mobile=post_data['mobile'],
                        marital_status=post_data['married_status'],
                        head_office='Y',
                        branch_no='0000',
                        memo=post_data['telephone'],
                        channel_payment=post_data['channel_payment'],
                        status='A',
                        occupation_id=post_data['occup'],
                        pre_name_id=prename_id,
                        slug=auto_slug(),
                        created_at=current_date,
                        updated_at=current_date,
                        refer_name=post_data['refer_name'],
                        refer_description=post_data['refer_description'],
                        refer_telephone=post_data['refer_telephone'],
                    )
                    customerInfo.save()

                try:
                    customerAddress = CustomerAddress.objects.filter(customer_id=customerInfo.id,address_id='1').first()
                except CustomerAddress.DoesNotExist:
                    customerAddress = None

                if customerAddress:
                    address_diffshift = post_data.get('address_diffshift', '')
                    if address_diffshift == 'true':
                        
                        province_name = post_data.get('province', '')
                        amphoe_name = post_data.get('amphoe', '')
                        tambon_name = post_data.get('tambon', '')
                        
                        address_master = MasterAddress(province_name, amphoe_name, tambon_name)
                        address = address_master.split('##')  # [0] จังหวัด, [1] อำเภอ, [2] ตำบล
                        province_customer = address[0] 
                        amphoe_customer = address[1] 
                        tambon_customer = address[2] 
                    else :
                        province_customer = post_data['province']
                        amphoe_customer = post_data['amphoe']
                        tambon_customer = post_data['tambon']
                        
                    postcode = post_data.get('postcode', '') 
                    if postcode == '' or not postcode.isdigit():
                        postcode = 0  
                        
                    customerAddress.send_doc = card_send_doc
                    customerAddress.house_no = post_data.get('address', '')  
                    customerAddress.village = post_data.get('village', '')
                    customerAddress.soi = post_data.get('soi', '')
                    customerAddress.road = post_data.get('road', '')
                    customerAddress.postcode = postcode
                    customerAddress.updated_at = current_date
                    customerAddress.amphoe_id = amphoe_customer
                    customerAddress.province_id = province_customer
                    customerAddress.tambon_id = tambon_customer
                    customerAddress.relate = post_data.get('relate', None)
                    customerAddress.save()
           
                else:
                    if post_data.get('address_diffshift', ''):
                        province_name = post_data.get('province', '')
                        amphoe_name = post_data.get('amphoe', '')
                        tambon_name = post_data.get('tambon', '')
                        address_master = MasterAddress(province_name, amphoe_name, tambon_name)
                        address = address_master.split('##') 
                          
                        province_customer = address[0] 
                        amphoe_customer = address[1] 
                        tambon_customer = address[2] 
                    else :
                        province_customer =  post_data['province']
                        amphoe_customer = post_data['amphoe']
                        tambon_customer = post_data['tambon']

                    postcode = post_data.get('postcode', '') 
                    if postcode == '' or not postcode.isdigit():
                        postcode = 0 

                    customerAddress = CustomerAddress.objects.create(
                        send_doc=card_send_doc,
                        house_no=post_data['address'],
                        village=post_data['village'],
                        soi=post_data['soi'],
                        road=post_data['road'],
                        postcode = postcode,
                        status='A',
                        slug=auto_slug(),
                        created_at=current_date,
                        updated_at=current_date,
                        amphoe_id=amphoe_customer,
                        customer_id=customerInfo.id,
                        province_id=province_customer,
                        tambon_id=amphoe_customer,
                        address_id='1',
                        relate=post_data['relate'],
                    )
                    customerAddress.save()
                try:
                    customerAddress2 = CustomerAddress.objects.filter(customer_id=customerInfo.id,address_id='2').first()
                except CustomerAddress.DoesNotExist:
                    customerAddress2 = None

                if customerAddress2:
                    if post_data.get('address_diffshift', ''):
                        province_name = post_data.get('province_current', '')
                        amphoe_name = post_data.get('amphoe_current', '')
                        tambon_name = post_data.get('tambon_current', '')

                        address_master = MasterAddress(province_name, amphoe_name, tambon_name)
                        address = address_master.split('##')
                        
                        province_customer = address[0] 
                        amphoe_customer = address[1] 
                        tambon_customer = address[2] 
                    else :
                        province_customer =  post_data['province_current']
                        amphoe_customer = post_data['amphoe_current']
                        tambon_customer = post_data['tambon_current']
                        
                    postcode = post_data.get('postcode_current', '') 
                    if postcode == '' or not postcode.isdigit():
                        postcode = 0 

                    customerAddress2.send_doc = current_send_doc
                    customerAddress2.house_no = post_data.get('address_current', '')
                    customerAddress2.village = post_data.get('village_current', '')
                    customerAddress2.soi = post_data.get('soi_current', '')
                    customerAddress2.road = post_data.get('road_current', '')
                    customerAddress2.postcode = postcode
                    customerAddress2.updated_at = current_date
                    customerAddress2.amphoe_id = amphoe_customer
                    customerAddress2.customer_id = customerInfo.id
                    customerAddress2.province_id = province_customer
                    customerAddress2.tambon_id = tambon_customer

                    customerAddress2.living_type_id = post_data.get('living_type_current', None)


                    customerAddress2.residence_id = post_data.get('residence_current', None)
                    customerAddress2.relate = post_data.get('relate_current', None)

                    customerAddress2.save()
                else:
                    address_diffshift = post_data.get('address_diffshift', '')
                    if address_diffshift == 'true':
                        
                        province_name = post_data.get('province_current', '')
                        amphoe_name = post_data.get('amphoe_current', '')
                        tambon_name = post_data.get('tambon_current', '')

                        address_master = MasterAddress(province_name, amphoe_name, tambon_name)
                        address = address_master.split('##')  # [0] จังหวัด, [1] อำเภอ, [2] ตำบล
                        
                        province_customer = address[0] 
                        amphoe_customer = address[1] 
                        tambon_customer = address[2] 
                    else :
                        province_customer =  post_data['province_current']
                        amphoe_customer = post_data['province_current']
                        tambon_customer = post_data['province_current']
                        
                    postcode = post_data.get('postcode_current', '') 
                    if postcode == '' or not postcode.isdigit():
                        postcode = 0 

                    customerAddress = CustomerAddress.objects.create(
                        send_doc=current_send_doc,
                        house_no=post_data['address_current'],
                        village=post_data['village_current'],
                        soi=post_data['soi_current'],
                        road=post_data['road_current'],
                        postcode=postcode,
                        status='A',
                        slug=auto_slug(),
                        created_at=current_date,
                        updated_at=current_date,
                        amphoe_id=amphoe_customer,
                        customer_id=customerInfo.id,
                        province_id=province_customer,
                        tambon_id=tambon_customer,
                        address_id='2',
                        living_type_id=post_data['living_type_current'],
                        residence_id= post_data.get('residence_current', None),
                        relate=post_data['relate_current'],
                    )
                    customerAddress.save()
                try:
                    customerAddress3 = CustomerAddress.objects.filter(customer_id=customerInfo.id,address_id='3').first()
                except CustomerAddress.DoesNotExist:
                    customerAddress3 = None

                if customerAddress3:
                    province_customer =  post_data.get('company_province', '')    
                    amphoe_customer = post_data.get('company_amphoe', '')
                    tambon_customer = post_data.get('company_tambon', '')
                    postcode = post_data.get('company_postcode', '') 
                    
                    if postcode == '' or not postcode.isdigit():
                        postcode = 0 

                    customerAddress3.send_doc = company_send_doc
                    customerAddress3.house_no = post_data.get('company_address', '')
                    customerAddress3.village = post_data.get('company_village', '')
                    customerAddress3.soi = post_data.get('company_soi', '')
                    customerAddress3.road = post_data.get('company_road', '')
                    customerAddress3.postcode = postcode
                    customerAddress3.updated_at = current_date
                    customerAddress3.amphoe_id = amphoe_customer
                    customerAddress3.customer_id = customerInfo.id
                    customerAddress3.province_id = province_customer
                    customerAddress3.tambon_id = tambon_customer
                    customerAddress3.relate = post_data.get('company_relate', '')

                    customerAddress3.save()

                else:
                    province_customer =  post_data.get('company_province', '')    
                    amphoe_customer = post_data.get('company_amphoe', '')
                    tambon_customer = post_data.get('company_tambon', '')
                    postcode = post_data.get('company_postcode', '') 
                        
                    if postcode == '' or not postcode.isdigit():
                        postcode = 0 

                    customerAddress = CustomerAddress.objects.create(
                        send_doc=company_send_doc,
                        house_no=post_data['company_address'],
                        village=post_data['company_village'],
                        soi=post_data['company_soi'],
                        road=post_data['company_road'],
                        postcode = postcode,
                        status='A',
                        slug=auto_slug(),
                        created_at=current_date,
                        updated_at=current_date,
                        amphoe_id=amphoe_customer,
                        customer_id=customerInfo.id,
                        province_id=province_customer,
                        tambon_id=tambon_customer,
                        address_id='3',
                        relate=post_data['company_relate'],
                    )
                    customerAddress.save()
               
                # if post_data['start_payment']:
                #     start_payment = formatDate(post_data['start_payment'])
                # else:
                #     start_payment = None

                bank_id = post_data.get('bank_id', None)

                try:
                        
                    if not id or not str(id).isdigit():  # ถ้า id เป็นค่าว่างหรือไม่ใช่ตัวเลข
                        installment = None
                    else:
                        installment = InstallmentDetail.objects.filter(id=int(id)).first() 

                except InstallmentDetail.DoesNotExist:
                    installment = None

                if installment:
                    base_income = post_data.get('base_income', '')
                    base_income_raw = base_income.replace(",", "") if base_income else ''
                    
                    installment.price = post_data.get('price', '')
                    installment.down_payment = post_data.get('down_payment', '')
                    installment.total = safe_decimal(post_data.get('net_amount', '0'))
                    installment.interest = safe_decimal(post_data.get('interest', '0'))
                    installment.installment = int(post_data.get('installment', 0))
                    # installment.start_payment = start_payment
                    installment.date_read_card = formatDate(post_data.get('read_card', ''))
                    installment.user_id = request.session.get('username', '')
                    installment.salary_day = post_data.get('salary_day', '')
                    installment.bank_id = bank_id
                    installment.place_of_work = post_data.get('place_of_work', '')
                    installment.created_at = current_date
                    installment.updated_at = current_date
                    installment.company_tel = post_data.get('company_tel', '')
                    installment.place_work_tel = post_data.get('place_work_tel', '')
                    installment.price_installment = post_data.get('price_installment', '')
                    installment.base_income = safe_decimal(base_income_raw)
                    installment.office = post_data.get('office', '')
                    installment.debt_in = safe_decimal(post_data.get('debt_in', '0'))
                    installment.debt_informal = safe_decimal(post_data.get('debt_informal', '0'))
                    installment.create_to_branch_id = post_data.get('branch', '')
                    installment.create_to_province_id = post_data.get('province_save', '')
                    installment.company_id = post_data.get('company_id', '')
                    installment.lending_description = post_data.get('lending_description', '')
                    installment.save()
                  
                else:
                  
                    base_income = post_data['base_income']
                    base_income_raw = base_income.replace(",", "")
                    installment = InstallmentDetail.objects.create(
                        app_id=app_id,
                        customer_id=customerInfo.id,
                        price=safe_decimal(post_data.get('price', '0')),  
                        down_payment=safe_decimal(post_data.get('down_payment', '0')),  
                        total=safe_decimal(post_data.get('net_amount', '0')),  
                        interest=safe_decimal(post_data.get('interest', '0')),  
                        installment=int(post_data.get('installment', 0)),  
                        # start_payment=start_payment,
                        date_read_card=formatDate(post_data.get('read_card', '')),
                        user_id=request.session.get('username', ''),
                        salary_day=post_data.get('salary_day', ''),
                        bank_id=bank_id,
                        place_of_work=post_data.get('place_of_work', ''),
                        created_at=current_date,
                        updated_at=current_date,
                        company_tel=post_data.get('company_tel', ''),
                        place_work_tel=post_data.get('place_work_tel', ''),
                        price_installment=post_data.get('price_installment', ''),
                        base_income=safe_decimal(base_income_raw),  
                        office=post_data.get('office', ''),
                        debt_in=safe_decimal(post_data.get('debt_in', '0')),  
                        debt_informal=safe_decimal(post_data.get('debt_informal', '0')),  
                        create_to_branch_id=post_data.get('branch', ''),
                        create_to_province_id=post_data.get('province_save', ''),
                        company_id=post_data.get('company_id', ''),
                        lending_description=post_data.get('lending_description', '')
                        
                    )
                    installment.save()

                try:
                    customerIncome = CustomerIncome.objects.filter(customer_id=customerInfo.id).first()

                except CustomerIncome.DoesNotExist:
                    customerIncome = None

                if customerIncome:
                    customerIncome.office = post_data['office']
                    customerIncome.user_id = request.session['user_id']
                    customerIncome.created_at = current_date
                    customerIncome.updated_at = current_date
                    customerIncome.save()
                else:
                    customerIncome = CustomerIncome.objects.create(
                        customer_id=customerInfo.id,
                        user_id=request.session['user_id'],
                        office=post_data['office'],
                        created_at=current_date,
                        updated_at=current_date,
                    )
                    customerIncome.save()

                
                file_index = 1  

                for file_key in request.FILES.keys():
                    if file_key.startswith('file_'):  
                        new_file_key = f'file_{file_index}'
                        
                        files = request.FILES.getlist(file_key)
                        file_id = int(file_key.split('_')[1])
                        
                        if files:
                            for file in files:
                                file_type_key = f'file_type_{file_index}'
                                file_type = request.POST.get(file_type_key, '')

                                try:
                                    installmentFileFilter = InstallmentFile.objects.filter(id=file_id).first()
                                except InstallmentFile.DoesNotExist:
                                    installmentFileFilter = None
                                
                                fs = FileSystemStorage()
                                
                                # สร้างชื่อไฟล์ใหม่โดยเพิ่ม timestamp
                                timestamp = int(time.time())
                                filename, file_extension = os.path.splitext(file.name)
                                new_filename = f"{filename}_{timestamp}{file_extension}"
                                
                                if installmentFileFilter:
                                    file_path = installmentFileFilter.name.path
                                    FileSystemStorage().delete(file_path)

                                    fs.save(new_filename, file)
                                    installmentFile = installmentFileFilter
                                    installmentFile.name = new_filename
                                    if file_type:
                                        installmentFile.type = file_type
                                        installmentFile.doc_id = file_type

                                    installmentFile.save()
                                else:
                                    fs.save(new_filename, file)
                                    installmentFile = InstallmentFile.objects.create(
                                        installment_id=installment.id,
                                        name=new_filename,
                                        type=file_type,
                                        doc_id=file_type 
                                    )
                                    installmentFile.save()

                            file_index += 1
                        else:
                            print(f"No files uploaded for {new_file_key}.")
                        
            messages.success(request, "บันทึกสำเร็จ")
            return redirect('/name-list')
           
        except DatabaseError as db_error:
            return JsonResponse({'error': str(db_error)}) 
       
    else:
        return JsonResponse({'error': 'fail insert'})
    
class DetailFileApiView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            page = int(request.GET.get('page', 1))
            pageSize = int(request.GET.get('pageSize', 10))

            queryset = InstallmentFile.objects.all()
            serializer = InstallmentFileSerializers(queryset, many=True)

            data = {
                'data': serializer.data[(page - 1) * pageSize:page * pageSize],
                'total': queryset.count()
            }

            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            page = int(request.data.get('page', 1))
            pageSize = int(request.data.get('pageSize', 10))

            queryset = InstallmentFile.objects.all()
            serializer = InstallmentFileSerializers(queryset, many=True)

            data = {
                'data': serializer.data[(page - 1) * pageSize:page * pageSize],
                'total': queryset.count()
            }

            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class updateStatus(BaseListAPIView):    
    def detail(request, id):
        status = request.POST.get('status')
        issue_cancel = request.POST.get('issue_cancel', '')
        
        current_date = datetime.now()
        installment_detail = InstallmentDetail.objects.get(id=id)
        installment_detail.status_approve = status
        installment_detail.approve_date = current_date
        installment_detail.user_approve = request.session['username']
        installment_detail.user_id = request.session['username']
        installment_detail.issue_cancel = issue_cancel
        installment_detail.save()

        return JsonResponse({'success': True, 'message': 'บันทึกข้อมูลสำเร็จ', 'detail': issue_cancel})
    
def DetailDeleteFile(request, file_id):
    if request.method == "GET":
        try:
            file = InstallmentFile.objects.get(id=file_id)
            file.delete()
            return JsonResponse({"success": True})
        except InstallmentFile.DoesNotExist:
            return JsonResponse({"success": False, "message": "File not found"})
    return JsonResponse({"success": True, "message": "File deleted successfully"})