from functools import wraps

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse as render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from utilis.function import BaseListAPIView,ListAPIView
from .models import MasterAuth, UserAuth ,MasterOfficer,AuthUser
from .serializers import AuthSerializer, MasterAuthSerializer, AuthListSerializer,MasterAuthUserSerializer,UserAuthSerializer


# Create your views here.
def check_permission(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user_auth = UserAuth.objects.filter(user=user, auth__auth_code='A005').first()
            if user_auth and not user_auth.status:
                return redirect('dashboard')

        return view_func(request, *args, **kwargs)

    return _wrapped_view


@check_permission
@login_required(login_url='/user_login')
def UserAuthPage(request):
    userauth = User.objects.all()
    return render(request, "userauth.html",{"users" :userauth} )

class userauthAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthSerializer

@check_permission
@login_required(login_url='/user_login')
def EditAuthPage(request, id_auth):
    userauth = UserAuth.objects.filter(user_id=id_auth)
    authname = MasterAuth.objects.all()
    user = User.objects.filter(id=id_auth).first()

    return render(request, "editauth.html", {'userauth': userauth, 'authname': authname, 'id': id_auth, 'user': user})


@api_view(['GET', 'POST'])
def UserAuthlist(request, id):
    try:
        user = User.objects.filter(id=id).first()
        userauth = UserAuth.objects.filter(user_id=user)

        if request.method == 'GET':
            serializer = AuthListSerializer(userauth, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':

            data = request.data
            auth_id = data['id']
            # status = data['status']
            if data['status'] == False:
                status = True
            else:
                status = False
            user_auth_instance = UserAuth.objects.filter(id=auth_id).first()

            user_auth_instance.status = status
            user_auth_instance.save()


            return JsonResponse({'success': True})

    except Exception as e:
        return Response({'error': str(e)}, status=500)


class UserList(BaseListAPIView):
    queryset = User.objects.all()
    serializer_class = AuthSerializer


class MasterAuthList(BaseListAPIView):
    queryset = MasterAuth.objects.all()
    serializer_class = MasterAuthSerializer


class AuthList(BaseListAPIView):
    queryset = AuthUser.objects.all().order_by('id')
    serializer_class = MasterAuthUserSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class editAuth(APIView):
    def get(self, request, id_auth):
        user_auth_queryset = UserAuth.objects.filter(user_id=id_auth).select_related("auth")  
        paginator = StandardResultsSetPagination()
        paginated_queryset = paginator.paginate_queryset(user_auth_queryset, request)
        serializer = AuthListSerializer(paginated_queryset, many=True)
        
        return paginator.get_paginated_response(serializer.data) 
        return render(request, "editauth.html", {'userauth': userauth, 'authname': authname, 'id': id_auth, 'user': user})


        