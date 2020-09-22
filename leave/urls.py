from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contactus/',views.contactus,name="contactus"),
    path('register/',views.register,name="register"),
    path('login/',views.login_url,name="login"),
    path('lstatus/',views.lstatus,name="lstatus"),
    path('logout/',views.logout_url,name="logout"),
    path('leaveform/',views.leaveform,name="leaveform"),
    path('approve/<int:id>/',views.approve_leave,name="approve"),
    path('decline/<int:id>/',views.decline_leave,name="decline"),
    #path('',views.,name=""),
]
