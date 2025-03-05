from django.urls import path

from exports import views
# from report.views import MasterBranchAPAPIView, apmastAPIView

app_name = 'exports'

urlpatterns = [
    path('exports_installment', views.exports_installment, name='exports_installment'),
#     path('MasterBranchAP/', MasterBranchAPAPIView.as_view(), name='MasterBranchAP'),
#     path('apmast/', apmastAPIView.as_view(), name='apmast'),
]
