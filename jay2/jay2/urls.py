from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from jay2.homeapp import views as home_views
from jay2.homeapp.forms import UserPasswordResetForm, UserLoginForm
from django.contrib.auth import views
# from django.contrib.auth.views import auth
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path(r'^dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    re_path(r'^dashboard/', TemplateView.as_view(template_name='dashboard.html'), name="dashboard"),
    re_path(r'^overdue/', TemplateView.as_view(template_name='overdue.html'), name="overdue"),
    re_path(r'^my_task/', TemplateView.as_view(template_name='my-task.html'), name="task"),
    re_path(r'^today/', TemplateView.as_view(template_name='today.html'), name="today"),
    re_path(r'^upcoming/', TemplateView.as_view(template_name='upcoming.html'), name="upcoming"),
    re_path(r'^archive/', TemplateView.as_view(template_name='archive.html'), name="archive"),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    path('password_reset/', views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',form_class=UserPasswordResetForm), name='password_reset'),
    path('login/', views.LoginView.as_view(template_name="registration/login.html", authentication_form=UserLoginForm), name='login'),
    re_path(r'^accounts/signup/$', home_views.register, name= "signup"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)