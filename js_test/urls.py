from django.contrib import admin
from django.urls import path, include
from js_test import views

urlpatterns = [
    path('', views.main, name='home'),
    path('detail', views.detail, name='detail')
]
