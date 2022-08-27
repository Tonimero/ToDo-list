from django.urls import path
from . import views
# from django.contrib import admin

urlpatterns = [
    # path('', views.firstpage),
    # path('about/', views.secondpage),
    # path('about/bio', views.thirdpage),
    # path('', views.index),
    path('user/', views.index, name='home'), 
    path('login-user/', views.login_user, name='login'), 
    path('register-user/', views.register_user, name='register'), 
    path('logout/', views.user_logout, name='logout'),
    
]