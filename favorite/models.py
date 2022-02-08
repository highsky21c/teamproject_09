from django.db import models
from user.models import UserModel


# Create your models here.
class Favorite(models.Model):
    class Meta:
        db_table = "favorite"
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=10) #가게정보


