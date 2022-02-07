from django.contrib.auth.models import AbstractUser #AbstractUser: 장고가 기본적으로 제공하는 auth_user과 연동되는 class
from django.db import models


#model.py 작성 후 -> makemigrations, migrate
class UserModel(AbstractUser): #AbstractUser기능을 UserModel에 사용
    class Meta:
        db_table = "my_user" #DB 테이블의 이름

    bio = models.CharField(max_length=256, default='') #상태메세지 추가 (장고에서 제공안함) -> settings.py 작성
    like_food = models.TextField(default='')