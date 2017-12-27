from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    openid = models.CharField(max_length=100, verbose_name='微信openid')
    nickname = models.CharField(max_length=20, verbose_name='昵称')
    gender = models.CharField(choices= (('1', '男'), ('0', '女')), max_length= 6, verbose_name='性别')
    avatarUrl = models.CharField(max_length=200, verbose_name='头像地址')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username