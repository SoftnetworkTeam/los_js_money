from django.urls import path
from django.conf.urls.static import static
from report import views
from .views import print_report

app_name = 'report'

urlpatterns = [
    path('report/<str:type>', views.report, name='report-type'),
    path('print_report/', views.print_report, name='print_report'),
]
urlpatterns += static('/configurations/js/', document_root='configurations/js/')