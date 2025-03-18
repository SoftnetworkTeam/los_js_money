from django.urls import path
from report import views
from .views import reports

app_name = 'report'

urlpatterns = [
    path('report/<str:type>', views.report, name='report-type'),
    path('report/', reports.as_view(), name='report'),
]
