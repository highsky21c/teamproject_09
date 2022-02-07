# contents/urls.py
from django.urls import path
from . import views

app_name = 'contents'


urlpatterns = [
    path('', views.home, name='home'),  # localhost:8000 과 views.py 폴더의 home 함수 연결
    path('contents/', views.contents, name='contents'),  # localhost:8000/contents 과 views.py 폴더의 contents 함수 연결
    path('contents/delete/<int:id>', views.delete_contents, name='delete-contents'),
    path('contents/<int:id>', views.detail_contents, name='detail-contents'),
    path('contents/comment/<int:id>', views.write_comment, name='write-comment'),
    path('contents/comment/delete/<int:id>', views.delete_comment, name='delete-comment'),
    path('contents/like/', views.like, name='like'),
    path('contents/hate/', views.hate, name='hate'),
]
