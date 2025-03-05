from utilis.function import BaseListAPIView
from rest_framework.generics import ListAPIView
from django.shortcuts import render, redirect
from functools import wraps
from django.contrib.auth.decorators import login_required
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count, Case, When, Value, IntegerField
from django.http import  JsonResponse,HttpResponseRedirect

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
            return Masterincomestable.objects.all().order_by("id")  

    
class MasterincomenotstableApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterincomenotstableSerializer
    def get_queryset(self):
        return Masterincomenotstable.objects.all().order_by("id")  

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
        ).order_by("id")

       
class MasterscoringdetailApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    queryset = Masterscoringdetail.objects.all()
    serializer_class = MasterscoringdetailSerializer
    
class MastercustomerageApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastercustomerageSerializer
    queryset = Mastercustomerage.objects.filter(status='A')
    
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
    queryset = Masterminorchildren.objects.filter(status='A')
        

class MastereducationlevelApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastereducationlevelSerializer
    queryset = Mastereducationlevel.objects.filter(status='A')
        
    
class MasterbusinesstypeApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterbusinesstypeSerializer
    queryset = Masterbusinesstype.objects.filter(status='A')
        

class MastershoptypesApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastershoptypesSerializer
    queryset = Mastershoptypes.objects.filter(status='A')
        
    
class MasterrentalageApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterrentalageSerializer
    queryset = Masterrentalage.objects.filter(status='A')
        
    
class MastermonthlyprofitApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastermonthlyprofitSerializer
    queryset = Mastermonthlyprofit.objects.filter(status='A')
        

class MasterbusinessageApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MasterbusinessageSerializer
    queryset = Masterbusinessage.objects.filter(status='A')
        
    
class MastercontractreasonApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastercontractreasonSerializer
    queryset = Mastercontractreason.objects.filter(status='A')
        

class MastercountryApiView(BaseListAPIView):
    pagination_class = NoLimitPagination
    serializer_class = MastercountrySerializer
    
    def get_queryset(self):
        queryset = Mastercountry.objects.all()

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
    queryset = Masterbusinesstype.objects.filter(status="A")
    
    



@method_decorator(csrf_exempt, name='dispatch')
class updateStatus(BaseListAPIView):    
    def post(self, request, *args, **kwargs):
        post_data = request.POST.dict()
        
        status_id = post_data.get('id')
        status = post_data.get('status')
        status_type = post_data.get('type')
        data_type = post_data.get('data_type')
        
        
        if status_type == "statusIncome" and data_type == "grade":
            Masterincomestable.objects.filter(id=status_id).update(status=status)
        elif status_type== "statusNotIncome" and data_type == "grade":
            Masterincomestable.objects.filter(id=status_id).update(status=status)
        elif status_type == "statusScoring" and data_type == "scoring":
            Masterscoringinfo.objects.filter(id=status_id).update(status=status)
        elif status_type == "statusUserauth":
            UserAuth.objects.filter(id=status_id).update(status=status)

            return JsonResponse({
                'status': 'success',
            })

        return JsonResponse({'status': 'failed', 'message': 'Invalid status type'})
 
def auto_slug():
    return datetime.now().strftime('%Y%m%d%H%M%S%f') 
    
class updateData(BaseListAPIView):
    def post(self, request, *args, **kwargs):
        post_data = request.POST.dict()
        
        print('request ssss',request.session['user_id'])
        
        data_type = post_data.get('data_type')
        type_button = post_data.get("type_button")
        
        now = datetime.now()
        
        if data_type == "grade" :
            grade_id = post_data.get("id")
            grade_code = post_data.get("grade_code")
            grade_type = post_data.get("type")
            
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
                    
        elif data_type == "scoring" :
            from decimal import Decimal
            
            print('request ssss',request.session['user_id'])

            score_id = post_data.get("id")
            score_name = post_data.get('score_name')
              # แปลงค่าเป็น Decimal ถ้าไม่สามารถแปลงได้ให้ใช้ค่า default เป็น 0
            stable_min = Decimal(post_data.get('stable_min', "0") or "0")
            stable_percent = Decimal(post_data.get('stable_percent', "0") or "0")
            not_stable_min = Decimal(post_data.get('not_stable_min', "0") or "0")
            not_stable_percent = Decimal(post_data.get('not_stable_percent', "0") or "0")
            
            if type_button == "save":
                updated = Masterscoringinfo.objects.filter(id=score_id).update(
                    score_name=score_name,
                    stable_min=stable_min,
                    stable_percent=stable_percent,
                    not_stable_min=not_stable_min,
                    not_stable_percent=not_stable_percent,
                    updated_at=now
                )
                if updated == 0:
                    grade = Masterscoringinfo(
                        id=score_id,
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
                    grade.save()
                    
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

                for scoring_type, (model, field) in scoring_type_mapping.items():
                    id = model.objects.filter(Q(status="A") & ~Q(**{field: ''})).values_list('id', flat=True)
                    
                    for tpye_id in id:
                        Masterscoringdetail.objects.create(
                            score_type=scoring_type,  
                            type_id=tpye_id,             
                            score=0.00,               
                            score_id=score_id,       
                            created_at=now,           
                            updated_at=now           
                        )
                    
                response_status = "save success"

            elif type_button == "delete":
                    grade = Masterscoringinfo.objects.get(id=grade_id)
                    grade.delete()
                    response_status = "delete success"
            
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
        scoring_id = self.request.query_params.get('id', None)

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
            "Z": "เกรดผู้มีรายได้ไม่สม่ำเสมอ"
        }

        scoring_details = Masterscoringdetail.objects.filter(score_id=scoring_id)

        scoring_summary = {
            item["score_type"]: item["count"]
            for item in scoring_details.values("score_type").annotate(count=Count("id"))
        }

        result = [
            {
                "id": index + 1,
                "score_type": score_type,
                "score_name": score_name,
                "count": scoring_summary.get(score_type, 0) 
            }
            for index, (score_type, score_name) in enumerate(sorted(scoringMap.items()))
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
        
        for s, t in zip(scores, type_id): #zip หรือจับคู่ไว้จับคู่
            scoring_detail = Masterscoringdetail.objects.filter(score_id=score_id, score_type=scoring_type, type_id=t).first()
            
            if scoring_detail:
                scoring_detail.score = s
                scoring_detail.updated_at = now
                scoring_detail.save()
           
        return Response({"message": "success"})
