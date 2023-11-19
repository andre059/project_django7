from rest_framework import viewsets, generics
from education.models import Lesson, Course
from education.serliazers import LessonSerializer, CourseSerializer

"""Класс на основе ViewSet для Course"""


class CourseViewSet(viewsets.ModelViewSet):
    """класс для вывода списка и информации по одному объекту"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    """Классы на основе generics для Lesson"""


class LessonCreateAPIView(generics.CreateAPIView):
    """создание сущности"""

    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """отображение списка сущностей"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """отображение одной сущности"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """редактирование сущности"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """удаление сущности"""

    queryset = Lesson.objects.all()
