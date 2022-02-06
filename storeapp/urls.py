from django.urls import path

from storeapp import views

app_name = 'storeapp'

urlpatterns = [
    path('create-data/', views.Save_Store_Data, name='creat-data'), #크롤링이 되는 페이지
]
