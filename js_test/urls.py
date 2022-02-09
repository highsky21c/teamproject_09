from django.contrib import admin
from django.urls import path, include
from js_test import views

urlpatterns = [
    path('', views.main, name='home'),
    path('detail/<str:store_name>', views.detail, name='detail'),
    path('sign-up/', views.join, name='sign-up'),
    path('sign-in/', views.login, name='login'),
    path('find-id/', views.findid, name='find-id'),
    path('find-id/find/', views.ajax_find_id_view, name='ajax_id'),
    path('find-pw', views.findpw, name='find-pw'),
    path('profile/', views.profile, name='profile'),
    path('store_db/', views.test_Store_data, name='test_Store'),
    path('comment/write/', views.write_comment, name='comment_write')
]