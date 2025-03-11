import base64
import json
import re
from django.conf import settings
from datetime import datetime
from functools import wraps
from urllib.parse import parse_qs, urlencode
import requests
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from requests.structures import CaseInsensitiveDict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from utilis.function import BaseListAPIView
from rest_framework.generics import ListAPIView
from configurations.views import Mastercountry

from theme.models import MasterProvince, MasterAmphoe, MasterTambon, \
    MasterCifDigit, \
    MasterCustomerPrename, MasterOccupation, apmast, MasterNCB,Masterincomestable,Masterincomenotstable,Masterscoringinfo,Mastercustomerage,Mastermaritalstatus,Masterminorchildren,Mastereducationlevel,Masterbusinesstype,Mastermonthlyprofit,Masterbusinessage,Mastercontractreason,MasterNumberOfInstallment,Mastershoptypes,Masterrentalage,MasterBank,Masterbranch,MasterContractDocument,LogUserLogin,Masterbranch, MasterCompany, UserBranch
from django.db.models import Q,OuterRef, Subquery
from userauth.models import UserAuth,AuthUser
from configurations.models import AuthUser
from .models import CustomerInfo, InstallmentDetail, CustomerLoanDetail, CustomerAddressDetail, \
    InstallmentFile
from django.contrib.auth.models import User
    
from .serializers import CustomerLoanDetailSerializer, InstallmentFileSerializers, MasterCustomerPrenameSerializer, MasterBranchAPSerializer, HireContract
from django.shortcuts import render, get_object_or_404


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
def base(request):
    user = request.user
    return render(request, "base.html", {'user': user})


def notfound():
    return render("notfound.html")


@login_required(login_url='/user_login')
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='/user_login')
def nameList(request):
    customer_loan_detail = CustomerLoanDetail.objects.all()
    return render(request, 'nameList.html', {'customer_loan_detail': customer_loan_detail})

# @login_required(login_url='/user_login')
# @check_permission

def configurations(request, grade_type=None):
    type_obj = []
    status_type = None
    data_type = None

    if grade_type == 'grade-income':
        type_obj = Masterincomestable.objects.all().order_by('id') 
        status_type = 'statusIncome'
        data_type = 'grade'
    elif grade_type == 'grade-unstable':
        type_obj = Masterincomenotstable.objects.all().order_by('id')
        status_type = 'statusNotIncome'
        data_type = 'grade'
    elif grade_type == 'scoring':
        type_obj = Masterscoringinfo.objects.all().annotate(
            first_name=Subquery(
                AuthUser.objects.filter(id=OuterRef('user_id')).values('first_name')[:1]
            )
        ).order_by("id")
        status_type = 'statusScoring'
        data_type = 'scoring'

    # โหลดข้อมูล user_admin ก่อนใช้
    user_admin = AuthUser.objects.all().order_by('id')

    if grade_type == 'scoring':
        # สร้าง dictionary ของ user_id -> username
        user_dict = {user.id: user.username for user in user_admin}

        # แปลง QuerySet เป็น list ของ dictionary
        type_obj = list(type_obj.values())

        # เพิ่ม username ให้แต่ละ item
        for item in type_obj:
            item["username"] = user_dict.get(item["user_id"], "ไม่พบข้อมูล")

    return render(request, 'configurations.html', {
        'grade_type': grade_type,
        'type_obj': type_obj, 
        'status_type' : status_type,
        'data_type' : data_type,
    })
       
@login_required(login_url='/user_login')
@check_permission
def configurationsDetail(request, id  ):
    user_admin = AuthUser.objects.filter(id=id).first()
    return render(request, 'configurationsDetail.html',{'user_admin' : user_admin})

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



@login_required(login_url='/user_login')
def detail(request, id):
    installment_obj = InstallmentDetail.objects.filter(id=id).first()
    installment_id = CustomerLoanDetail.objects.filter(id=id).first()
    customerid = installment_id.customer_id
    
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
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

    customer_loan_detail = CustomerLoanDetail.objects.filter(id=id).first()
    customer_info = CustomerInfo.objects.filter(id=customerid).first()
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
        'loan_status': loan_status
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
        customer = CustomerLoanDetail.objects.filter(id=id).first(),
        formatted_date_time_birth_date = format_date_time(customer_info.birth_date),
        formatted_date_time_issue_date = format_date_time(customer_info.issue_date),
        formatted_date_time_expire_date = format_date_time(customer_info.expire_date)
        formatted_date_time_date_read_card = format_date_time(installment.date_read_card)
        formatted_date_time_start_payment = format_date_time(installment.start_payment)
        
        country = Mastercountry.objects.filter(id=customer_info.country_id).first()
        bank = MasterBank.objects.filter(id=installment.bank_id).first()
        province_branch = MasterProvince.objects.filter(id=installment.create_to_province_id).first()
        branch = Masterbranch.objects.filter(id=installment.create_to_branch_id).first()
        
        file_objects = InstallmentFile.objects.filter(installment_id=installment.id).select_related('doc')

        for file_type in file_objects:
            print(vars(file_type) )

    
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

def user_login(request):
    if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=name, password=password)
        auth_user = AuthUser.objects.filter(username=name).first()
        full_name = auth_user.first_name + ' ' + auth_user.last_name

        if user is not None:
            auth_login(request, user)
            request.session['username'] = user.username
            request.session['alert_login'] = 'success'
            request.session['user_id'] = user.id
            
            mid_user_auth = UserAuth.objects.filter(user=user)
            if mid_user_auth.exists():
                for foo in mid_user_auth:
                    if foo.auth.auth_code == 'A007':
                        if not foo.status:
                            return render(request, "login.html",
                                          {'msg': 'คุณไม่มีสิทธิ์ใช้งานระบบนี้', 'show_alert': True})

            user_branch = UserBranch.objects.filter(user_id=user.id, status=True)
            master_branch = Masterbranch.objects.filter(
                id__in=[ub.branch_id for ub in user_branch]
            )
            # print("Masterbranch:", [ub.branch_id for ub in user_branch])
            master_company = MasterCompany.objects.filter(
                id__in=[mb.company_id for mb in master_branch]
            )
            # print("Companies:", [mb.company_id for mb in master_branch])
            
            request.session['master_company'] = [company.id for company in master_company]
            request.session['master_branch'] = [branch.id for branch in master_branch]

            return render(request, "login.html", {
                'show_branch_modal': True,
                'master_company': master_company,
                'master_branch': master_branch,
                'user_id' : user.id,
                'username' : user.username,
                'name' : full_name
            })

        else:
            return render(request, "login.html", {'msg': 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง'})
    else:
        return render(request, "login.html")

def save_branch(request):
    if request.method == 'POST':
        try:
            user_id = request.POST.get('user_id')
            company_id = request.POST.get('company')
            branch_id = request.POST.get('branch')
            
            branch = Masterbranch.objects.filter(id=branch_id).first()
            
            request.session['company_id'] = company_id 
            request.session['branch_id'] = branch_id
            request.session['branch_province_id'] = branch.province_id

            if not user_id or not company_id or not branch_id:
                return JsonResponse({'status': 'error', 'message': 'error'}, status=400)

            now = datetime.now()
            updated = LogUserLogin.objects.filter(user_id=user_id).update(
                company_id=company_id,
                branch_id=branch_id
            )
            if updated == 0:
                grade = LogUserLogin(
                    user_id=user_id,
                    company_id=company_id,
                    branch_id=branch_id,
                    created_at=now,
                    updated_at=now
                )
                grade.save()

            return JsonResponse({'status': 'success'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
def clear_alert_login(request):
    
        if request.session['alert_login'] == 'success':
            
            request.session['alert_login'] = 'other success'
            return JsonResponse({'status': 'success'})

def logout_view(request):
    logout(request)
    return redirect('/user_login')

# ฟังก์ชั่นการทำงาน
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
    customer_info = CustomerInfo.objects.filter(cust_code__startswith=search_digit,
                                                conversion_id__isnull=True).order_by('-cust_code').first()
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
    latest_installment = InstallmentDetail.objects.filter(app_id__startswith=formatted_current_date).order_by(
        '-id').first()
    if latest_installment:
        latest_app_id = latest_installment.app_id
        running_no = latest_app_id[-4:]
        new_running_no = str(int(running_no) + 1).zfill(4)
        app_id = latest_app_id[:-4] + new_running_no
    else:
        app_id = formatted_current_date + '0001'

    return app_id


def MasterAddress(province_name: str, amphoe_name: str, tambon_name: str):
    province = MasterProvince.objects.filter(province_name=province_name).first()
    if province:
        province_id = province.id

    else:
        # ไม่พบข้อมูลจังหวัดที่ตรงกับเงื่อนไข
        return None

    amphoe = MasterAmphoe.objects.filter(amphoe_name=amphoe_name, province_id=province_id).first()
    if amphoe:
        amphoe_id = amphoe.id

    else:
        # ไม่พบข้อมูลอำเภอที่ตรงกับเงื่อนไข
        return None

    tambon = MasterTambon.objects.filter(tambon_name=tambon_name, amphoe_id=amphoe_id).first()

    if tambon:
        tambon_id = tambon.id

    else:
        # ไม่พบข้อมูลตำบลที่ตรงกับเงื่อนไข
        return None

    return str(province_id) + '##' + str(amphoe_id) + '##' + str(tambon_id)

def formatDate(date_str):
    if date_str:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
        return formatted_date

def DetailDeleteFile(request, file_id):
    if request.method == "GET":
        try:
            file = InstallmentFile.objects.get(id=file_id)
            file.delete()
            return JsonResponse({"success": True})
        except InstallmentFile.DoesNotExist:
            return JsonResponse({"success": False, "message": "File not found"})
    return JsonResponse({"success": True, "message": "File deleted successfully"})


def EditDeleteFile(request, file_id):
    file = InstallmentFile.objects.get(id=file_id)
    installment_id = file.installment_id
    file.delete()

    return redirect('edit', installment_id)

