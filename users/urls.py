from django.urls import path

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import CourseViewSet, LessonViewSet, UserCreateAPIView

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'lessons', LessonViewSet, basename='lessons')

urlpatterns = [
    path('users/create/', UserCreateAPIView.as_view(), name='users-create'),
] + router.urls
