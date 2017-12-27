from datetime import datetime

from django.db import models

from wx_user.models import User
from pictures.models import Picture


# Create your models here.
class UserPicture(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')
    picture = models.ForeignKey(Picture, verbose_name='作品')

    class Meta:
        verbose_name = '用户收藏的作品'
        verbose_name_plural = verbose_name
        unique_together = ("user", "picture")

    def __str__(self):
        return self.user.nickname + '-' + self.picture.name
