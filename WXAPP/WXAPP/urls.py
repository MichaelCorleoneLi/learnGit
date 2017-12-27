"""WXAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from Courses.views import CoursesListViewSet
from teachers.views import TeachersListViewSet
from pictures.views import PicturesListViewSet
from studyCourse.views import UserCourseViewSet
from userPicture.views import UserPictureViewSet
from wx_user.views import login, UserViewSet
from WXAPP.settings import MEDIA_ROOT

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name="users")
router.register(r'courses', CoursesListViewSet, base_name='courses')
router.register(r'teachers', TeachersListViewSet, base_name='teachers')
router.register(r'pictures', PicturesListViewSet, base_name='pictures')
router.register(r'userCourse', UserCourseViewSet, base_name='userCourse')
router.register(r'userPicture', UserPictureViewSet, base_name='userPicture')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #课程列表页s
    url(r'^', include(router.urls)),
    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
    #drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    #第三方登录（微信小程序）
    #url('', include('social_django.urls', namespace='social')),
]
