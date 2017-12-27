import xadmin
from xadmin import views

from .models import Teacher


class TeacherAdmin(object):
    pass

xadmin.site.register(Teacher, TeacherAdmin)