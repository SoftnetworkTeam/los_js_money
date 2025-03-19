from django.urls import path
from django.conf.urls.static import static
from userauth import views
from .views import MasterAuthList, AuthList, editAuth, UserList,UserList

app_name = 'userauth'

urlpatterns = [
    # path("userauthpage", views.UserAuthPage, name='userauthpage'),
    path("userauth/", views.UserAuthPage, name='userauth'),
    path("userauth-api/", UserList.as_view(), name='userauth-api'),
    path("user-api/", UserList.as_view(), name='user-api'),
    
    path("userauth/edit/<id_auth>/", views.EditAuthPage, name='editauth'),
    path("masterauth-api/", MasterAuthList.as_view(), name='masterauth-api'),
    path("authlist-api/", AuthList.as_view(), name='authlist-api'),
    path('edit-auth-api/<int:id_auth>/', editAuth.as_view(), name='edit-auth-api'),
]
urlpatterns += static('/userauth/js/', document_root='userauth/js/')

