from rest_framework import serializers

from education.models import Lesson, Course
from education.services import convert_currencies
from education.validators import LinkVideoValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkVideoValidator('video_link')]  # проверка этого поля на регулярное выражение


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)  # Подгрузка данных из связанных моделей
    usd_prise = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.id).count()

    def get_usd_prise(self, instance):
        return convert_currencies(instance.price)
