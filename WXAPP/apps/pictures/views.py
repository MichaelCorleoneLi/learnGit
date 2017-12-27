from time import time

from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from PIL import Image

from .models import Picture
from .serializers import PicturesSerializer

# Create your views here.
class PicturesPagination(PageNumberPagination):
    page_size = 6
    page_size_query_description = 'page_size'
    page_query_param = 'page'
    max_page_size = 100

class PicturesListViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,
                          mixins.DestroyModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    展画列表
    """
    queryset = Picture.objects.all()
    serializer_class = PicturesSerializer
    pagination_class = PicturesPagination

    def create(self, request, *args, **kwargs):
        picture = request.FILES['uploadPicture']
        newPicture = Picture()
        newPicture.image = picture
        newPicture.author = request.user
        newPicture.save()
        return Response("添加成功")