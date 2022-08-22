from xml.etree.ElementInclude import include
from django.urls import path
from . import views
# from django.contrib import admin

urlpatterns = [
    # path('', views.firstpage),
    # path('about/', views.secondpage),
    # path('about/bio', views.thirdpage),
    # path('', views.index),
    path('', views.index, name='index'), 
    path('create-task/', views.create_task, name='create-task'), 
    
    
]