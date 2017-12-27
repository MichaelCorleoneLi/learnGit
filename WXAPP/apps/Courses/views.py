from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Course
from .serializers import CoursesSerializer
# Create your views here.

class CoursesPagination(PageNumberPagination):
    page_size = 3
    page_size_query_description = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class CoursesListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    课程列表页
    """
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    pagination_class = CoursesPagination
