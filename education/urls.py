from education.apps import EducationConfig
from education.views import LessonViewSet, CourseViewSet
from rest_framework.routers import DefaultRouter


app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'lesson', LessonViewSet, basename='lesson')

urlpatterns = [

] + router.urls
