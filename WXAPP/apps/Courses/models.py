from datetime import datetime

from django.db import models
from teachers.models import Teacher

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    teacher = models.ForeignKey(Teacher, verbose_name='讲师', null=True, blank=True)
    degree = models.CharField(choices=(('cj','初级'), ('zj','中级'), ('gj','高级')), verbose_name='难度', max_length=5)
    students = models.IntegerField(default=0, verbose_name='学习人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
