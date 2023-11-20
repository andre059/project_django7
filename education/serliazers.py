from rest_framework import serializers
from education.models import Lesson, Course


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()  #  кастомизация поля lessons_count

    def get_lessons_count(self, obj):
        return obj.lessons_count

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
