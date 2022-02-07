# user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):

#model.py 작성 후 -> makemigrations, migrate
class UserModel(AbstractUser): #AbstractUser기능을 UserModel에 사용

    class Meta:

        db_table = "my_user"
    bio = models.CharField(max_length=256, default='')
