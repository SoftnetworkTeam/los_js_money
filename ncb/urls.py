from django.urls import path
from ncb import views
from .views import NcbApiView

app_name = 'ncb'

urlpatterns = [
    path("/ncb",views.ncb, name='ncb'),
    path("/addNcb",views.addNcb, name='add_ncb'),
    path("/editNCB/<id>",views.editNCB, name='edit_ncb'),
    path('/ncb-api', NcbApiView.as_view(), name='ncb-api'),
]