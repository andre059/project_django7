from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from users.serliazers import UserSerializer, PaymentsSerializer, PaymentsHistorySerializer
from users.models import User, Payments, PaymentsHistory


class UserViewSet(viewsets.ModelViewSet):
    """класс для вывода списка и информации по одному объекту"""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    """Классы на основе generics для Payments"""


class PaymentsCreateAPIView(generics.CreateAPIView):
    """создание сущности"""

    serializer_class = PaymentsSerializer


class PaymentsListAPIView(generics.ListAPIView):
    """отображение списка сущностей"""

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payment_date',)
    ordering_fields = ('payment_method', 'course',)


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    """отображение одной сущности"""

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()


class PaymentsUpdateAPIView(generics.UpdateAPIView):
    """редактирование сущности"""

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()


class PaymentsDestroyAPIView(generics.DestroyAPIView):
    """удаление сущности"""

    queryset = Payments.objects.all()

    """Классы на основе generics для PaymentsHistory"""


class PaymentsHistoryCreateAPIView(generics.CreateAPIView):
    """создание сущности"""

    serializer_class = PaymentsHistorySerializer


class PaymentsHistoryListAPIView(generics.ListAPIView):
    """отображение списка сущностей"""

    serializer_class = PaymentsHistorySerializer
    queryset = PaymentsHistory.objects.all()


class PaymentsHistoryRetrieveAPIView(generics.RetrieveAPIView):
    """отображение одной сущности"""

    serializer_class = PaymentsHistorySerializer
    queryset = PaymentsHistory.objects.all()


class PaymentsHistoryUpdateAPIView(generics.UpdateAPIView):
    """редактирование сущности"""

    serializer_class = PaymentsHistorySerializer
    queryset = PaymentsHistory.objects.all()


class PaymentsHistoryDestroyAPIView(generics.DestroyAPIView):
    """удаление сущности"""

    queryset = Payments.objects.all()
