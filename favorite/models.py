from django.db import models
from user.models import UserModel
from storeapp.models import Store


# Create your models here.
class Favorite(models.Model):
    class Meta:
        db_table = "favorite"
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)



