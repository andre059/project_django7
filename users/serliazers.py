from rest_framework import serializers
from users.models import User, Payments, PaymentsHistory


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
