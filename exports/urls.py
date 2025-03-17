from django.urls import path
from exports import views
from .views import exports

app_name = 'exports'

urlpatterns = [
    path('export/<str:type>', views.export, name='export'),
    path('exports/', exports.as_view(), name='exports'),
    
]
