from utilis.function import BaseListAPIView
from rest_framework.generics import ListAPIView
from django.shortcuts import render, redirect
from functools import wraps
from django.contrib.auth.decorators import login_required
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count, Case, When, Value, IntegerField
from django.http import  JsonResponse,HttpResponseRedirect
from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime

# models
from .models import  AuthUser,Masterscoringdetail,Mastermonthlysalary,Mastereducationlevel,Masterminorchildren,Masterworkingage,Mastercustomerage,Mastershoptypes,Masterrentalage,Mastermaritalstatus,Mastercustomerage,Mastershoptypes,Masterrentalage,Masterbusinesstype,Mastermonthlyprofit,Masterbusinessage,Mastercontractreason,Mastercountry
from userauth.models import UserAuth,MasterAuth
from django.db.models import OuterRef, Subquery, Value, FloatField, F,DecimalField,Count,Q
from django.db.models.functions import Coalesce
from theme.models import Masterincomestable,Masterincomenotstable,Masterscoringinfo,MasterOccupation,MasterResidence,MasterOccupation,MasterLivingType,MasterBranchAP

# serializers
from .serializers import MasterscoringdetailSerializer,MastercustomerageSerializer,MasterminorchildrenSerializer,MasterbusinesstypeSerializer,MastershoptypesSerializer,MasterrentalageSerializer,MastermonthlyprofitSerializer,MasterbusinessageSerializer,MastercontractreasonSerializer,MastereducationlevelSerializer,MastercountrySerializer
from theme.serializers import MasterincomestableSerializer,MasterincomenotstableSerializer,MasterscoringinfoSerializer,MasterBranchAPSerializer
from nameList.serializers import MasterResidenceSerializer


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

# @login_required(login_url='/user_login')
# @check_permission

def configurations(request, grade_type=None):
    type_obj = []
    status_type = None
    data_type = None

    if grade_type == 'grade-income':
        type_obj = Masterincomestable.objects.all() 
        status_type = 'statusIncome'
        data_type = 'grade'
    elif grade_type == 'grade-unstable':
        type_obj = Masterincomenotstable.objects.all()
        status_type = 'statusNotIncome'
        data_type = 'grade'
    elif grade_type == 'scoring':
        type_obj = Masterscoringinfo.objects.all().annotate(
            first_name=Subquery(
                AuthUser.objects.filter(id=OuterRef('user_id')).values('first_name')[:1]
            )
        )
        status_type = 'statusScoring'
        data_type = 'scoring'

    user_admin = AuthUser.objects.all()

    if grade_type == 'scoring':
        user_dict = {user.id: user.username for user in user_admin}

        type_obj = list(type_obj.values())

        for item in type_obj:
            item["username"] = user_dict.get(item["user_id"], "ไม่พบข้อมูล")

    return render(request, 'configurations.html', {
        'grade_type': grade_type,
        'type_obj': type_obj, 
        'status_type' : status_type,
        'data_type' : data_type,
    })
       

def configurationsDetail(request, id):
    scoringinfo = Masterscoringinfo.objects.filter(id=id).first()
    
    if not scoringinfo:
        return redirect('dashboard') 
    
    return render(request, 'configurationsDetail.html', {'scoringinfo': scoringinfo})
    
class NoLimitPagination(PageNumberPagination):
    page_size = 1000  
    
class MasterincomestableApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterincomestableSerializer
    def get_queryset(self):
            return Masterincomestable.objects.all()  

    
class MasterincomenotstableApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterincomenotstableSerializer
    def get_queryset(self):
        return Masterincomenotstable.objects.exclude(status='C')

class MasterscoringinfoApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterscoringinfoSerializer
    
    def get_queryset(self):
        return Masterscoringinfo.objects.filter(status='A')
    
class AdminscoringinfoApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterscoringinfoSerializer
    
    def get_queryset(self):
        return Masterscoringinfo.objects.filter(status='A').annotate(
            first_name=Subquery(
                AuthUser.objects.filter(id=OuterRef('user_id')).values('first_name')[:1]
            )
        )

       
class MasterscoringdetailApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    queryset = Masterscoringdetail.objects.all()
    serializer_class = MasterscoringdetailSerializer
    
class MastercustomerageApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastercustomerageSerializer
    
    def get_queryset(self):
        queryset = Mastercustomerage.objects.filter(status='A')
        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(age_name__icontains=query_param))

        return queryset
    
class rangeAge(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastercustomerageSerializer
    queryset = Mastercustomerage.objects.filter(status='A')

    def get_queryset(self):
        age = self.request.GET.get('age')
        if age:
            age = int(age) 
            queryset = Mastercustomerage.objects.filter(
                start_age__lte=age,  
                end_age__gte=age   
            )

        return queryset


    
class MasterminorchildrenApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterminorchildrenSerializer
    
    def get_queryset(self):
        queryset = Masterminorchildren.objects.filter(status='A')
        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(children_name__icontains=query_param))

        return queryset
        

class MastereducationlevelApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastereducationlevelSerializer
    
    def get_queryset(self):
        queryset = Mastereducationlevel.objects.filter(status='A')
        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(education_name__icontains=query_param))

        return queryset
        
    
class MasterbusinesstypeApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterbusinesstypeSerializer
    
    def get_queryset(self):
        queryset = Masterbusinesstype.objects.filter(status='A')

        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(business_type_name__icontains=query_param))

        return queryset
        

class MastershoptypesApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastershoptypesSerializer
    
    def get_queryset(self):
        queryset = Mastershoptypes.objects.filter(status='A')

        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(shop_name__icontains=query_param))

        return queryset
        
    
class MasterrentalageApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterrentalageSerializer
    
    def get_queryset(self):
        queryset = Masterrentalage.objects.filter(status='A')

        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(age_name__icontains=query_param))

        return queryset
        
    
class MastermonthlyprofitApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastermonthlyprofitSerializer
    
    def get_queryset(self):
        queryset = Mastermonthlyprofit.objects.filter(status='A')

        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(profit_name__icontains=query_param))

        return queryset
        

class MasterbusinessageApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterbusinessageSerializer
    queryset = Masterbusinessage.objects.filter(status='A')
    
    def get_queryset(self):
        queryset = Masterbusinessage.objects.filter(status='A')

        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(age_name__icontains=query_param))

        return queryset
        
    
class MastercontractreasonApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastercontractreasonSerializer
    
    def get_queryset(self):
        queryset = Mastercontractreason.objects.filter(status='A')

        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(reason_name__icontains=query_param))

        return queryset
        

class MastercountryApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastercountrySerializer
    
    def get_queryset(self):
        queryset = Mastercountry.objects.all()
        
        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(nation_name_th__icontains=query_param))

        order_by = [
            'ไทย', 'จีน', 'ลาว', 'พม่า', 'เวียดนาม', 
            'สหรัฐอเมริกา', 'สิงคโปร์', 'เกาหลีใต้', 'ญี่ปุ่น', 'ฮ่องกง'
        ]
        
        order_case = Case(
            *[When(nation_name_th=country, then=Value(i)) for i, country in enumerate(order_by)],
            default=Value(len(order_by)),  
            output_field=IntegerField()
        )

        return queryset.annotate(order_by=order_case).order_by('order_by', 'nation_name_th')
    
    
    queryset = Masterscoringinfo.objects.all().annotate(
        username=Subquery(
            AuthUser.objects.filter(id=OuterRef('user_id')).values('username')[:1]
        )
    )

class businesstypeApiView(BaseListAPIView):    
    pagination_class = NoLimitPagination
    serializer_class = MasterbusinesstypeSerializer
    
    def get_queryset(self):
        queryset = Masterbusinesstype.objects.filter(status='A')

        query_param = self.request.query_params.get('q', None)
        
        if query_param:
            queryset = queryset.filter(Q(business_type_name__icontains=query_param))

        return queryset
    

@method_decorator(csrf_exempt, name='dispatch')
class updateStatus(BaseListAPIView):    
    def post(self, request, *args, **kwargs):
        post_data = request.POST.dict()
        
        status_id = post_data.get('id')
        status = post_data.get('status')
        status_type = post_data.get('type')
        
        
        if status_type == "statusIncome" :
            Masterincomestable.objects.filter(id=status_id).update(status=status)
        elif status_type== "statusNotIncome" :
            Masterincomenotstable.objects.filter(id=status_id).update(status=status)
        elif status_type == "statusScoring" :
            Masterscoringinfo.objects.filter(id=status_id).update(status=status)
        elif status_type == "statusUserauth":
            UserAuth.objects.filter(id=status_id).update(status=status)

        return JsonResponse({'status': 'success'})

        # return JsonResponse({'status': 'failed', 'message': 'Invalid status type'})
 
def auto_slug():
    return datetime.now().strftime('%Y%m%d%H%M%S%f') 
    
class updateData(BaseListAPIView):
    def post(self, request, *args, **kwargs):
        post_data = request.POST.dict()
        
        data_type = post_data.get('data_type')
        type_button = post_data.get("type_button")
        
        now = datetime.now()
        
        if data_type == "grade" :
            grade_id = post_data.get("id",None)
            grade_code = post_data.get("grade_code")
            grade_type = post_data.get("type")
            
            if grade_type == "statusIncome":
                model_class = Masterincomestable
            elif grade_type == "statusNotIncome":
                model_class = Masterincomenotstable
                
            if type_button == "save":
                if grade_id :
                    model_class.objects.filter(id=grade_id).update(
                        grade_code=grade_code,
                        updated_at=now
                    )
                else :
                    grade = model_class(
                        grade_code=grade_code,
                        status="A",
                        slug=auto_slug(),
                        created_at=now,
                        updated_at=now
                    )
                    grade.save()
                response_status = "save success"

            elif type_button == "delete":
                    grade = model_class.objects.get(id=grade_id)
                    grade.delete()
                    response_status = "delete success"
                    
        elif data_type == "scoring" :
            from decimal import Decimal
            score_id = post_data.get("id",None)
            score_name = post_data.get('score_name')
            stable_min = Decimal(post_data.get('stable_min', "0") or "0")
            stable_percent = Decimal(post_data.get('stable_percent', "0") or "0")
            not_stable_min = Decimal(post_data.get('not_stable_min', "0") or "0")
            not_stable_percent = Decimal(post_data.get('not_stable_percent', "0") or "0")
            
            if type_button == "save":
                if score_id:
                    Masterscoringinfo.objects.filter(id=score_id).update(
                        score_name=score_name,
                        stable_min=stable_min,
                        stable_percent=stable_percent,
                        not_stable_min=not_stable_min,
                        not_stable_percent=not_stable_percent,
                        updated_at=now
                    )
                    response_status = "save success"
                else:
                    score = Masterscoringinfo(
                        user_id=request.session['user_id'],
                        score_name=score_name,
                        stable_min=stable_min,
                        stable_percent=stable_percent,
                        not_stable_min=not_stable_min,
                        not_stable_percent=not_stable_percent,
                        status="A",
                        slug=auto_slug(),
                        created_at=now,
                        updated_at=now
                    )
                    score.save()  

                    score_id = score.id 

                    scoring_type_mapping = {
                        'A': (MasterOccupation, 'occup_name'),
                        'B': (Mastermonthlysalary, 'salary_name'),
                        'C': (Mastereducationlevel, 'education_name'),
                        'D': (Masterminorchildren, 'children_name'),
                        'E': (Masterworkingage, 'age_name'),
                        'F': (Mastercontractreason, 'reason_name'),
                        'G': (MasterResidence, 'residence_name'),
                        'H': (MasterLivingType, 'type_name'),
                        'I': (Mastermaritalstatus, 'status_name'),
                        'J': (Mastercustomerage, 'age_name'),
                        'K': (Mastershoptypes, 'shop_name'),
                        'L': (Masterrentalage, 'age_name'),
                        'M': (Masterbusinesstype, 'business_type_name'),
                        'N': (Mastermonthlyprofit, 'profit_name'),
                        'O': (Masterbusinessage, 'age_name'),
                        'Y': (Masterincomestable, 'grade_code'),
                        'Z': (Masterincomenotstable, 'grade_code'),
                    }

                    with transaction.atomic():  # transaction เป็นคำสั่งที่เอาไว้เช็คว่าข้อมูลที่ต้องการจะบันทึกได้บันทึกลงดาต้าเบสถูกต้องแล้วหรือไม่ ถ้าไม่ถูกต้องจะยกเลิกการบันทึกและ rollback กลับมา
                        new_scoringdetail = []  # เก็บข้อมูลลงอาเรย์เพื่อเตรียมบันทึกลงดาต้าเบส

                        for scoring_type, (model, field) in scoring_type_mapping.items():
                            new_ids = model.objects.filter(Q(status="A") & ~Q(**{field: ''})).values_list('id', flat=True)

                            for type_id in new_ids:
                                new_scoringdetail.append(Masterscoringdetail(
                                    score_type=scoring_type,
                                    type_id=type_id,
                                    score=0.00,
                                    score_id=score_id,
                                    created_at=now,
                                    updated_at=now
                                ))

                        # ใช้ bulk_create เพื่อเพิ่มข้อมูลทีเดียว
                        if new_scoringdetail:
                            Masterscoringdetail.objects.bulk_create(new_scoringdetail)
                            response_status = "save success"

            elif type_button == "delete":
                count_row = Masterscoringinfo.objects.count()  

                if count_row > 1:
                    Masterscoringinfo.objects.get(id=score_id).delete()
                    Masterscoringdetail.objects.filter(score_id=score_id).delete()
                    response_status = "delete success"
                else:
                    response_status = "can't delete"
            
        return JsonResponse({'status': response_status})
        
class updateScoring(BaseListAPIView):
    def post(self, request, *args, **kwargs):
        post_data = request.POST.dict()
        
        grade_id = post_data.get("id")
        grade_code = post_data.get("grade_code")
        grade_type = post_data.get("type")
        type_button = post_data.get("type_button")
        now = datetime.now()
        
        if grade_type == "statusIncome":
            model_class = Masterincomestable
        elif grade_type == "statusNotIncome":
            model_class = Masterincomenotstable
        
        if type_button == "save":
            updated = model_class.objects.filter(id=grade_id).update(
                grade_code=grade_code,
                updated_at=now
            )
            if updated == 0:
                grade = model_class(
                    id=grade_id,
                    grade_code=grade_code,
                    status="A",
                    slug=auto_slug(),
                    created_at=now,
                    updated_at=now
                )
                grade.save()
            response_status = "save success"

        elif type_button == "delete":
                grade = model_class.objects.get(id=grade_id)
                grade.delete()
                response_status = "delete success"
            
        return JsonResponse({'status': response_status})
  

class scoringListApiView(ListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterscoringdetailSerializer

    def get_queryset(self):
        scoring_id = self.request.query_params.get("id", None)

        if not scoring_id:
            return []

        scoringMap = {
            "A": "ประเภทอาชีพ",
            "B": "เงินเดือนประจำ",
            "C": "ระดับการศึกษา",
            "D": "บุตรที่ยังไม่บรรลุนิติภาวะ",
            "E": "อายุงาน",
            "F": "วัตถุประสงค์",
            "G": "ประเภทที่พักอาศัย",
            "H": "สถานะที่พักอาศัย",
            "I": "สถานะครอบครัว",
            "J": "อายุผู้สมัคร",
            "K": "ประเภทร้านค้า",
            "L": "อายุการเช่า",
            "M": "ลักษณะธุรกิจ",
            "N": "กำไรต่อเดือน",
            "O": "อายุธุรกิจ",
            "Y": "เกรดผู้มีรายได้ประจำ",
            "Z": "เกรดผู้มีรายได้ไม่สม่ำเสมอ",
        }

        scoring_details = Masterscoringdetail.objects.filter(score_id=scoring_id)

        scoring_summary = {
            item["score_type"]: item["count"]
            for item in scoring_details.values("score_type").annotate(count=Count("id"))
        }

        query_param = self.request.query_params.get("q", None)

        filter_scoringMap = {
            type : score_type
            for type, score_type in scoringMap.items()
            if query_param is None or query_param.lower() in score_type.lower()
        }

        result = [
            {
                "id": index + 1,
                "score_type": score_type,
                "score_name": score_name,
                "count": scoring_summary.get(score_type, 0),
            }
            for index, (score_type, score_name) in enumerate(sorted(filter_scoringMap.items()))
        ]

        return result


class ViewScoringDetailApiView(ListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterscoringdetailSerializer

    def get_queryset(self):
        scoring_id = self.request.query_params.get('id', None)
        scoring_type = self.request.query_params.get('scoring_type', None)

        if not scoring_id or not scoring_type:
            return Masterscoringdetail.objects.none()

        scoring_type_mapping = {
            'A': (MasterOccupation, 'occup_name'),
            'B': (Mastermonthlysalary, 'salary_name'),
            'C': (Mastereducationlevel, 'education_name'),
            'D': (Masterminorchildren, 'children_name'),
            'E': (Masterworkingage, 'age_name'),
            'F': (Mastercontractreason, 'reason_name'),
            'G': (MasterResidence, 'residence_name'),
            'H': (MasterLivingType , 'type_name'),
            'I': (Mastermaritalstatus, 'status_name'),
            'J': (Mastercustomerage, 'age_name'),
            'K': (Mastershoptypes, 'shop_name'),
            'L': (Masterrentalage, 'age_name'),
            'M': (Masterbusinesstype, 'business_type_name'),
            'N': (Mastermonthlyprofit, 'profit_name'),
            'O': (Masterbusinessage, 'age_name'),
            'Y': (Masterincomestable, 'grade_code'),
            'Z': (Masterincomenotstable, 'grade_code'),
        }

        if scoring_type not in scoring_type_mapping:
            return Masterscoringdetail.objects.none()

        master_model, name_field = scoring_type_mapping[scoring_type]

        master_queryset = master_model.objects.filter(Q(status="A") & ~Q(**{name_field: ''})).annotate(
            score_id=Value(scoring_id),
            score_type=Value(scoring_type),
            name=F(name_field),
            score=Coalesce(
                Subquery(
                    Masterscoringdetail.objects.filter(
                        score_id=scoring_id,
                        score_type=scoring_type,
                        type_id=OuterRef('id')
                    ).values('score')[:1]
                ),
                Value(0, output_field=DecimalField()) 
            )
        ).values(
            'id', 'score_id', 'score_type', 'name', 'score'
        )
        
        if scoring_type in ['Y', 'Z']:
            master_queryset = master_queryset.order_by('name')

        return master_queryset



class updateConfig(APIView):
    def post(self, request, *args, **kwargs):
        post_data = request.data  
        now = datetime.now()  

        score_id = post_data.get('score_id')  
        scoring_type = post_data.get('scoring_type')  
        type_id = post_data.getlist('type_id[]')  
        scores = post_data.getlist('score[]')  
        stable_min = post_data.get('stable_min') 
        stable_percent = post_data.get('stable_percent') 
        not_stable_min = post_data.get('not_stable_min') 
        not_stable_percent = post_data.get('not_stable_percent') 
        
        if score_id:
            Masterscoringinfo.objects.filter(id=score_id).update(
                user_id=request.session['user_id'],
                stable_min=stable_min,
                stable_percent=stable_percent,
                not_stable_min=not_stable_min,
                not_stable_percent=not_stable_percent,
                status="A",
                updated_at=now
            )
        
        for s, t in zip(scores, type_id): #zip จับคู่
            scoring_detail = Masterscoringdetail.objects.filter(score_id=score_id, score_type=scoring_type, type_id=t).first()
            
            if scoring_detail:
                scoring_detail.score = s
                scoring_detail.updated_at = now
                scoring_detail.save()
           
        return Response({"message": "success"})
