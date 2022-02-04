from django.db import models


# Create your models here.
class Favorite(models.Model):
    class Meta:
        db_table = "favorite"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)


