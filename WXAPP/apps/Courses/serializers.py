from rest_framework import serializers

from .models import Course
from teachers.serializers import TeachersSerializer

class CoursesSerializer(serializers.ModelSerializer):
    teacher = TeachersSerializer()
    class Meta:
        model = Course
        fields = "__all__"