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
    company_id = request.session.get('company_id')
    create_to_branch_id = request.session.get('branch_id')

    installment_all = InstallmentDetail.objects.filter(company_id=company_id,create_to_branch_id=create_to_branch_id).count()
    installment_approve = InstallmentDetail.objects.filter(status_approve=1, company_id=company_id,create_to_branch_id=create_to_branch_id).count()
    installment_waiting = InstallmentDetail.objects.filter(status_approve__isnull=True, company_id=company_id,create_to_branch_id=create_to_branch_id).count()
    
    return render(request, 'dashboard.html', {
        'installment_all': installment_all,
        'installment_approve': installment_approve,
        'installment_waiting': installment_waiting,
    })

def user_login(request):
    if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=name, password=password)
        auth_user = AuthUser.objects.filter(username=name).first()

        if user is not None:
            auth_login(request, user)
            full_name = auth_user.first_name + ' ' + auth_user.last_name
            
            request.session['username'] = user.username
            request.session['alert_login'] = 'success'
            request.session['user_id'] = user.id
            
            check_userlogin = LogUserLogin.objects.filter(user_id=user.id).first()
            check_branch_name = Masterbranch.objects.filter(id=check_userlogin.branch_id).first()
            
            user_branch = UserBranch.objects.filter(user_id=user.id, status=True)
            master_branch = Masterbranch.objects.filter(id__in=[ub.branch_id for ub in user_branch])
            master_company = MasterCompany.objects.filter(id__in=[mb.company_id for mb in master_branch])
            
            request.session['master_company'] = [company.id for company in master_company]
            request.session['master_branch'] = [branch.id for branch in master_branch]

            return render(request, "login.html", {
                'show_branch_modal': True,
                'master_company': master_company,
                'master_branch': master_branch,
                'user_id': user.id,
                'username': user.username,
                'name': full_name,
                'check_userlogin' : check_userlogin,
                'check_branch_name' : check_branch_name,
            })

        else:
            return render(request, "login.html", {'msg': 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง'})
    else:
        return render(request, "login.html")

def select_branch(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        company_id = request.POST.get('company_id')

        if company_id:
            master_branch = request.session.get('master_branch', [])
            branch = Masterbranch.objects.filter(company_id=company_id, id__in=master_branch)
            branch_list = [{'id': branch.id, 'branch_name': branch.branch_code+' - '+branch.branch_name} for branch in branch]

            return JsonResponse({'branch': branch_list})

    
def save_branch(request):
    if request.method == 'POST':
        try:
            user_id = request.POST.get('user_id')
            company_id = request.POST.get('company')
            branch_id = request.POST.get('branch')
            
            company = MasterCompany.objects.filter(id=company_id).first()
            branch = Masterbranch.objects.filter(id=branch_id).first()
            
            company_name = company.company_name
            company_name = company_name.replace("บริษัท ", "")
            
            request.session['company_id'] = company_id 
            request.session['branch_id'] = branch_id
            request.session['company_name'] = company_name
            request.session['branch_name'] = branch.branch_name
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

def EditDeleteFile(request, file_id):
    file = InstallmentFile.objects.get(id=file_id)
    installment_id = file.installment_id
    file.delete()

    return redirect('edit', installment_id)

