from django.db import models

from wx_user.models import User
from Courses.models import Course
# Create your models here.
class UserCourse(models.Model):
    user = models.ForeignKey(User, verbose_name='学生')
    course = models.ForeignKey(Course, verbose_name='课程')

    class Meta:
        verbose_name = '学生学习的课程'
        verbose_name_plural = verbose_name
        unique_together = ("user", "course")

    def __str__(self):
        return self.user.nickname + "-" + self.course.name