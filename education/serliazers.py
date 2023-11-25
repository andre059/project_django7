from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from education.models import Lesson, Course
from education.validators import LinkVideoValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        # permission_classes = [IsAuthenticated]  # требует аутентификации пользователя для доступа к объектам модели
        validators = [LinkVideoValidator('video_link')]  # проверка этого поля на регулярное выражение


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)  # Подгрузка данных из связанных моделей

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.id).count()

    class Meta:
        model = Course
        fields = '__all__'
        # permission_classes = [IsAuthenticated]  # требует аутентификации пользователя для доступа к объектам модели
