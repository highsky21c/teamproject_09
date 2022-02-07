# contents/models.py
from django.db import models
from user.models import UserModel
from django.conf import settings


# Create your models here.
class ContentsModel(models.Model):

    class Meta:

        db_table = "contents"
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    subject = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,  # this is preferred than just 'User'
        blank=True,  # blank is allowed
        related_name='likes_user'
    )  # likes_user field

    hates_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,  # this is preferred than just 'User'
        blank=True,  # blank is allowed
        related_name='hates_user'
    )  # hates_user field

    def count_likes_user(self): #total likes_user
        return self.likes_user.count()

    def count_hates_user(self):
        return self.hates_user.count()


class ContentsComment(models.Model):
    class Meta:
        db_table = "comment"
    contents = models.ForeignKey(ContentsModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    cmt_likes_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='cmt_likes_user'
    )
    cmt_hates_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='cmt_hates_user'
    )

    def cmt_count_likes_user(self):
        return self.cmt_likes_user.count()

    def cmt_count_hates_user(self):
        return self.cmt_hates_user.count()

