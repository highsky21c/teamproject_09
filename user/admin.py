from django.contrib import admin #admin tool 사용
from .models import UserModel #동일한 위치에 있는 models 파일에서 UserModel을 import

# Register your models here.
admin.site.register(UserModel) # UserModel(models.py 작성)을 Admin에 추가 -> 관리자화면에 적용