from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'), # 헤더에서 로그아웃눌렀을때 로그아웃시켜주기!
    path('logout/', views.logout, name='logout'),
    path('find-id/', views.findid, name='find-id'),
    path('find-id/find/', views.ajax_find_id_view, name='ajax_id'),
    path('profile/', views.profile, name='profile'),
]
