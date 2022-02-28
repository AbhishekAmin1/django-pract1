from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from group import views

urlpatterns = [
    path('add/', views.group),
    path('contactUs/', views.contactUs),
    path('', views.index),
]