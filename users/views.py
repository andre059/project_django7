from rest_framework import viewsets, generics

from users.models import Course, Lesson
from users.serliazers import CourseSerializer, LessonSerializer, UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
