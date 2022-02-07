from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'), #sign-up/로 들어가면 view파일에 있는 sign_up_view 실행
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/', views.logout, name='logout'),
    # front에서 특정 주소로 데이터보내야한다!
]