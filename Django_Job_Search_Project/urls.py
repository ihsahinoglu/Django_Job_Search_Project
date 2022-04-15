"""Django_Job_Search_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views
from user import views as UserViews

urlpatterns = [
                  path('', include('home.urls')),
                  path('home/', include('home.urls')),
                  path('user/', include('user.urls'), name='user'),

                  path('contactus/', views.contactus, name='contactus'),
                  path('job-details/<slug:slug>/', views.jobDetails, name='job-details'),
                  path('job-list/', views.jobList, name='job-list'),
                  path('create-resume/', views.createResume, name='create-resume'),
                  path('company-info/', views.companyInfo, name='company-info'),
                  path('post-a-job/', views.PostJob, name='post-a-job'),
                  path('company-detail/<slug:slug>/', views.companyDetail, name='company-detail'),
                  path('candidates-profile/', views.candidatesProfile, name='candidates-profile'),
                  path('login/', UserViews.login_form, name='login'),
                  path('company-login/', UserViews.company_login_form, name='company-login'),
                  path('signup/', UserViews.signup_form, name='signup'),
                  path('company-signup/', UserViews.company_signup_form, name='company-signup'),
                  path('logout/', UserViews.logout_func, name='logout'),
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
