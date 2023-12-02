from rest_framework import serializers
from stripe import Subscription

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
    subscribers_count = serializers.SerializerMethodField(read_only=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.id).count()

    def get_usd_prise(self, instance):
        return convert_currencies(instance.price)

    def get_subscribers_count(self, instance):
        return instance.subscription_set.all().count()

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        try:
            Subscription.objects.get(subscriber=request.user, course=obj)
            return 'Подписан'
        except Subscription.DoesNotExist:
            return 'Не подписан'
