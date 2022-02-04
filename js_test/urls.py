from django.contrib import admin
from django.urls import path, include
from js_test import views

urlpatterns = [
    path('', views.main, name='home'),
    path('detail', views.detail, name='detail'),
    path('sign-up/', views.join, name='sign-up'),
    path('sign-in/', views.login, name='login'),
    path('find-id/', views.findid, name='find-id'),
    path('find-pw/', views.findpw, name='find-pw'),
    path('profile/', views.profile, name='profile'),
]
