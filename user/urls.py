from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/',views.logout,name='logout'),
    path('profile/', views.show_profile, name='profile'),
    path('home/', views.show_home, name='home'),
]
