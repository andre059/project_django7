from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from users.models import User, Payments, PaymentsHistory, CourseSubscription


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'


class PaymentsHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentsHistory
        fields = '__all__'


class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = '__all__'
