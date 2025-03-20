from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from . import views
from theme import views

urlpatterns = [
    # path("", views.index, name='index'),
    path("", views.dashboard, name='dashboard'),
    path("dashboard",views.dashboard,  name='dashboard'),
    path('clear_alert_login/', views.clear_alert_login, name='clear_alert_login'),
    path("notfound/<id>", views.notfound, name='notfound'),
    path("user_login", views.user_login),
    path('save_branch/', views.save_branch),
    path("logout", views.logout_view, name="logout"),
    path("select_branch/", views.select_branch, name="select_branch"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
