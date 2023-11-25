from rest_framework import viewsets, generics
from education.models import Lesson, Course
from education.paginators import EducationPaginator
from education.serliazers import LessonSerializer, CourseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.permissions import IsUserOrStaff, UserIsStaff

"""Класс на основе ViewSet для Course"""


class CourseViewSet(viewsets.ModelViewSet):
    """класс для вывода списка и информации по одному объекту"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [AllowAny]
    pagination_class = EducationPaginator

    """Классы на основе generics для Lesson"""


class LessonCreateAPIView(generics.CreateAPIView):
    """создание сущности"""

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonListAPIView(generics.ListAPIView):
    """отображение списка сущностей"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = EducationPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """отображение одной сущности"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """редактирование сущности"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsUserOrStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """удаление сущности"""

    queryset = Lesson.objects.all()
    permission_classes = [UserIsStaff]
