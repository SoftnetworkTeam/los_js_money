from datetime import datetime
from functools import wraps

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from theme.models import MasterNCB
from theme.models import apmast
from userauth.models import UserAuth
from utilis.function import BaseListAPIView
from .serializers import MasterNCBSerializer


# Create your views here.
def check_permission(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user_auth = UserAuth.objects.filter(user=user, auth__auth_code='A002').first()
            if user_auth and not user_auth.status:
                return redirect('index')

        return view_func(request, *args, **kwargs)

    return _wrapped_view

def check_permission2(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user_auth = UserAuth.objects.filter(user=user, auth__auth_code='A003').first()
            if user_auth and not user_auth.status:
                return redirect('index')

        return view_func(request, *args, **kwargs)

    return _wrapped_view

@login_required(login_url='/user_login')
def ncb(request):
    return render(request, "ncb/ncb.html")


@login_required(login_url='/user_login')
@check_permission2
def addNcb(request):
    if request.method == 'POST':
        current_date = datetime.now()
        saveNCB = MasterNCB.objects.create(
            name=request.POST['name'],
            description=request.POST['desc'],
            status=request.POST['status'],
            slug=auto_slug(),
            created_at=current_date,
            updated_at=current_date
        )
        saveNCB.save()

        return redirect('/ncb/ncb')

    else:
        ap = apmast.objects.filter()
        return render(request, 'ncb/addNcb.html')


@login_required(login_url='/user_login')
@check_permission
def editNCB(request, id):
    if request.method == 'POST':
        current_date = datetime.now()
        try:
            ncbEdit = MasterNCB.objects.get(id=id)
            ncbEdit.name = request.POST.get('name')
            ncbEdit.description = request.POST.get('desc')
            ncbEdit.status = request.POST.get('status')
            ncbEdit.updated_at = current_date
            ncbEdit.save()

            return redirect('/ncb/ncb')
        except MasterNCB.DoesNotExist:
            return render(request, 'ncb/editNcb.html', {'error': 'Record not found'})

    else:
        ncb = MasterNCB.objects.filter(id=id).first()
        return render(request, 'ncb/editNcb.html', {'all_data': ncb})


class NcbApiView(BaseListAPIView):
    queryset = MasterNCB.objects.all()
    serializer_class = MasterNCBSerializer


def auto_slug():
    return datetime.now().strftime('%Y%m%d%H%M%S%f')
