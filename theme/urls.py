from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from . import views

from theme import views
from nameList.views import CustomerLoanDetailApiView

urlpatterns = [
    # path("", views.index, name='index'),
    path("", views.dashboard, name='dashboard'),
    path("dashboard",views.dashboard,  name='dashboard'),
    path('clear_alert_login/', views.clear_alert_login, name='clear_alert_login'),
    path('name-list', views.nameList, name='name-list'),
    path("name-list/detail/<id>", views.detail, name='detail'),
    path("name-list/edit/<id>", views.editFormcommon, name='edit'),
    path("name-list/create", views.createCustomer, name='name-list_create'),
    re_path(r"^edit/$", views.createCustomer, name="editoldcar"),
    path("detaildelete/<int:file_id>/", views.DetailDeleteFile, name='detaildelete_file'),
    path("configurations/<str:grade_type>",views.configurations,  name='configurations'),
    path("configurations/<str:grade_type>/create", views.configurations, name='grade-low'),
    path('name-list', views.nameList, name='nameList'),
    path('customer-api/', CustomerLoanDetailApiView.as_view(), name='customer_loan_d_api'),
    path("notfound/<id>", views.notfound, name='notfound'),
    path("user_login", views.user_login),
    path('save_branch/', views.save_branch),
    path("logout", views.logout_view, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
