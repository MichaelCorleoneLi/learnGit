from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.CharField(choices=(('male','男'), ('female','女')), max_length=6, verbose_name='性别')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name