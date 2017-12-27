from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Teacher
from .serializers import TeachersSerializer


# Create your views here.
class TeachersPagination(PageNumberPagination):
    page_size = 3
    page_size_query_description = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class TeachersListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    教师列表页
    """
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer
    pagination_class = TeachersPagination