from rest_framework import serializers
from education.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)  # Подгрузка данных из связанных моделей

    class Meta:
        model = Course
        fields = '__all__'
