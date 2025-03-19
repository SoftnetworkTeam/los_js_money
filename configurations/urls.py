from django.urls import path
from django.conf.urls.static import static
from configurations import views
from .views import MasterincomestableApiView,MasterincomenotstableApiView,MasterscoringinfoApiView,MasterscoringinfoApiView,ViewScoringDetailApiView,MasterscoringdetailApiView,scoringListApiView,updateStatus,updateData,AdminscoringinfoApiView,updateConfig
from nameList.views import MasterOccupationAPIView

app_name = 'configurations'

urlpatterns = [
    path("configurations/<str:grade_type>",views.configurations,  name='configurations'),
    path("configurations/<str:grade_type>/create", views.configurations, name='grade-low'),
    path('/Masterincomestable/', MasterincomestableApiView.as_view(), name='Masterincomestable'),
    path('/Masterincomenotstable/', MasterincomenotstableApiView.as_view(), name='Masterincomenotstable'),
    path('/Masterscoringinfo/', AdminscoringinfoApiView.as_view(), name='Masterscoringinfo'),
    path("configurations/detail/<id>",views.configurationsDetail,  name='configurations'),
    path('/MasterOccupation/', MasterOccupationAPIView.as_view(), name='MasterOccupation'),
    path('Masterscoringdetail/', MasterscoringdetailApiView.as_view(), name='Masterscoringdetail'),
    path('/scoringinfo/', MasterscoringinfoApiView.as_view(), name='scoringinfo'),
    path('scoringView/', ViewScoringDetailApiView.as_view(), name='scoringView'),
    path('scoringList/', scoringListApiView.as_view(), name='scoringList'),
    path('updateStatus/', updateStatus.as_view(), name='updateStatus'),
    path('updateData/', updateData.as_view(), name='updateData'),
    path('updateConfig/', updateConfig.as_view(), name='updateConfig'),
]

urlpatterns += static('/configurations/js/', document_root='configurations/js/')