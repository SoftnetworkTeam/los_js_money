from django.urls import path,re_path
from django.conf.urls.static import static
from nameList import views
from .views import  MasterOfficerAPIView, MasterBrandAPIView, MasterModelAPIView, MasterSubModelAPIView,MasterColorAPIView,interestAPIView, MasterNumberOfInstallmentAPIView, MasterCustomerPrenameAPIView, MasterOccupationAPIView, MasterProvinceAPIView, MasterAmphoeAPIView, MasterTambonAPIView, MasterResidenceAPIView, MasterLivingOwnerAPIView, MasterLivingTypeAPIView, MasterBankAPIView, MasterContractDocumentAPIView, HireContractApiView,CustomerLoanDetailApiView,branchAPAPIView,CalScoring,updateStatus,CustomerLoanDetailApiView

from configurations.views import MastercustomerageApiView,MasterminorchildrenApiView,MastereducationlevelApiView,businesstypeApiView,MastershoptypesApiView,MasterrentalageApiView,MastermonthlyprofitApiView,MasterbusinessageApiView,MastercontractreasonApiView,MastercountryApiView,MasterscoringinfoApiView,rangeAge
app_name = 'nameList'

urlpatterns = [
    path('name-list', views.nameList, name='name-list'),
    path('customer-api/<str:status>/', CustomerLoanDetailApiView.as_view(), name='customer-api-status'),
    path('name-list/approve', views.nameList, name='name-list-approve'),
    path('name-list/waiting', views.nameList, name='name-list-waiting'),
    path("name-list/detail/<id>", views.detail, name='detail'),
    path("name-list/edit/<id>", views.editFormcommon, name='edit'),
    path("name-list/create", views.createCustomer, name='name-list_create'),
    re_path(r"^edit/$", views.createCustomer, name="editloan"),
    path("detaildelete/<int:file_id>/", views.DetailDeleteFile, name='detaildelete_file'),  
    path('MasterOfficer/', MasterOfficerAPIView.as_view(), name='MasterOfficer'),
    path('MasterModel/', MasterModelAPIView.as_view(), name='MasterModel'),
    path('MasterSubModel/', MasterSubModelAPIView.as_view(), name='MasterSubModel'),
    path('MasterColor/', MasterColorAPIView.as_view(), name='MasterColor'),
    path('interest/', interestAPIView.as_view(), name='interest'),
    path('MasterNumberOfInstallment/', MasterNumberOfInstallmentAPIView.as_view(), name='MasterNumberOfInstallment'),
    path('MasterCustomerPrename/', MasterCustomerPrenameAPIView.as_view(), name='MasterCustomerPrename'),
    path('MasterOccupation/', MasterOccupationAPIView.as_view(), name='MasterOccupation'),
    path('MasterProvince/', MasterProvinceAPIView.as_view(), name='MasterProvince'),
    path('MasterAmphoe/', MasterAmphoeAPIView.as_view(), name='MasterAmphoe'),
    path('MasterTambon/', MasterTambonAPIView.as_view(), name='MasterTambon'),
    path('MasterResidence/', MasterResidenceAPIView.as_view(), name='MasterResidence'),
    path('MasterLivingOwner/', MasterLivingOwnerAPIView.as_view(), name='MasterLivingOwner'), 
    path('MasterLivingType/', MasterLivingTypeAPIView.as_view(), name='MasterLivingType'),
    path('MasterBank/',MasterBankAPIView.as_view(), name='MasterBank'),
    path('MasterContractDocument/',MasterContractDocumentAPIView.as_view(), name='MasterContractDocument'),
    path("insertInstallment", views.insertInstallment, name='insertInstallment'),
    path("hireContractApi/", HireContractApiView.as_view(), name='hireContractApi' ),
    path('MasterBrandRef/', MasterBrandAPIView.as_view(), name='MasterBrandRef'),
    path('Mastercustomerage/', MastercustomerageApiView.as_view(), name='Mastercustomerage'),
    path('Mastereducationlevel/', MastereducationlevelApiView.as_view(), name='Mastereducationlevel'),
    path('Masterminorchildren/', MasterminorchildrenApiView.as_view(), name='Masterminorchildren'),
    path('businesstype/', businesstypeApiView.as_view(), name='businesstype'),
    path('Mastershoptypes/', MastershoptypesApiView.as_view(), name='Mastershoptypes'),
    path('Masterrentalage/', MasterrentalageApiView.as_view(), name='Masterrentalage'),
    path('Mastermonthlyprofit/', MastermonthlyprofitApiView.as_view(), name='Mastermonthlyprofit'),
    path('Masterbusinessage/', MasterbusinessageApiView.as_view(), name='Masterbusinessage'),
    path('Mastercontractreason/', MastercontractreasonApiView.as_view(), name='Mastercontractreason'),
    path('Masterbranch/', branchAPAPIView.as_view(), name='Masterbranch'),
    path('Mastercountry/', MastercountryApiView.as_view(), name='Mastercountry'),
    path('Masterscoringinfo/', MasterscoringinfoApiView.as_view(), name='Masterscoringinfo'),
    path('cal-scoring/', CalScoring.as_view(), name='cal-scoring'),
    path('updateStatus/', updateStatus.as_view(), name='updateStatus'),
    path('rangeAge/', rangeAge.as_view(), name='rangeAge'),
]

urlpatterns += static('/nameList/js/', document_root='nameList/js/')