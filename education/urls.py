from django.urls import path
from education.apps import EducationConfig
from education.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView
from rest_framework.routers import DefaultRouter


app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    # Lesson
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete'),
] + router.urls
