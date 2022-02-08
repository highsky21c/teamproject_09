from django.db import models


# Create your models here.

# class Savetore_text(models.Model):
#     class Meta:
#         db_table = "stores"
#
#     store_name = models.CharField(max_length=256, blank=True)
#     address = models.CharField(max_length=256, blank=True)
#     web_link = models.URLField()
#     operating_time = models.CharField(max_length=256, blank=True)
#     last_order = models.CharField(max_length=256, blank=True)
#     break_time = models.CharField(max_length=256, blank=True)
#     holiday = models.CharField(max_length=256, blank=True)
#     pic = '' # 이미지 리스트로 저장해야함
#     menu = ''  # 메뉴 딕셔너리
#     kind_of_food = models.CharField(max_length=256, blank=True)
#     price_range = models.CharField(max_length=256, blank=True)
#     phone_num = models.CharField(max_length=256, blank=True)
#     parking = models.CharField(max_length=256, blank=True)


class Store(models.Model):
    store_name = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=45)
    last_order = models.CharField(max_length=45)
    web_link = models.CharField(max_length=150)
    operating_time = models.CharField(max_length=150)
    break_time = models.CharField(max_length=45)
    holiday = models.CharField(max_length=45)
    pic = models.TextField()
    menu = models.TextField()
    kind_of_food = models.CharField(max_length=100)
    price_range = models.CharField(max_length=45)
    parking = models.CharField(max_length=100)

    class Meta:
        db_table = 'Store'


class SaveStore(models.Model):
    class Meta:
        db_table = "stores"

    store = models.TextField(null=True)

#
#
# class SaveSubCategory(models.Model):
#     class Meta:
#         db_table = 'subcategory'
#
#     subtitle = models.CharField(max_length=256)
#     stores = models.TextField(null=True)
