from django.db import models


# Create your models here.
class Favorite(models.Model):
    class Meta:
        db_table = "favorite"
    user = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=10) #가게정보


