from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('load', views.load_favorite, name='load_favorite'),
    path('add', views.add_favorite, name='add_favorite')
]