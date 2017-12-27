from django.db import models
from datetime import datetime

from wx_user.models import User

# Create your models here.
class Picture(models.Model):
    author = models.ForeignKey(User, verbose_name='作者')
    image = models.ImageField(upload_to='pictures/%Y/%m', verbose_name='画', max_length=200)
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    zan_nums = models.IntegerField(default=0, verbose_name='点赞人数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '画展'
        verbose_name_plural = verbose_name
