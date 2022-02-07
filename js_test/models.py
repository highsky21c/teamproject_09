from django.db import models


# Create your models here.
class Store(models.Model):
    store_name = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=45)
    last_order = models.CharField(max_length=45)
    web_link = models.CharField(max_length=150)
    operating_time = models.CharField(max_length=150)
    break_time = models.CharField(max_length=45)
    holiday = models.CharField(max_length=45)
    pic = models.CharField(max_length=500)
    menu = models.CharField(max_length=200)
    kind_of_food = models.CharField(max_length=100)
    price_range = models.CharField(max_length=45)
    parking = models.CharField(max_length=100)

    class Meta:
        db_table = 'Store'
