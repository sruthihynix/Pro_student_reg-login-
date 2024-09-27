
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.reg_page,name='registration'),
    path('registration/',views.reg_page,name='registration'),
    path('login/',views.login_page,name='login'),
    path('log_btn/', views.log_btn,name='log_btn'),
    path('home/',views.home_page,name='home'),
    path('show/',views.show_students,name='show'),
    path('logout/',views.logout_page,name='logout'),
]
