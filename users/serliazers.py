from rest_framework import serializers

from users.models import User, Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
