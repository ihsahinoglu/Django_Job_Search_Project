from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('index/', views.index, name='index'),
    #path('contactus/', views.contactus, name='contactus'),
    #path('job-details/', views.jobDetails, name='job-details')
]
