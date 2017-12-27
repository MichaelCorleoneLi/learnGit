from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserCourse
from Courses.serializers import CoursesSerializer


class UserCourseDetailSerializer(serializers.ModelSerializer):
    course = CoursesSerializer()
    class Meta:
        model = UserCourse
        fields = "__all__"

class UserCourseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserCourse
        validators = [
            UniqueTogetherValidator(
                queryset=UserCourse.objects.all(),
                fields = ('user', 'course'),
                message='已添加到课程'
            )
        ]
        fields = "__all__"