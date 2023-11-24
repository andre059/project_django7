from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from users.permissions import UserIsStaff, IsUserOrStaff
from users.serliazers import UserSerializer, PaymentsSerializer, PaymentsHistorySerializer, CourseSubscriptionSerializer
from users.models import User, Payments, PaymentsHistory, CourseSubscription


class UserViewSet(viewsets.ModelViewSet):
    """класс для вывода списка и информации по одному объекту"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    """Классы на основе generics для Payments"""


class PaymentsCreateAPIView(generics.CreateAPIView):
    """создание сущности"""

    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]


class PaymentsListAPIView(generics.ListAPIView):
    """отображение списка сущностей"""

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payment_date',)
    ordering_fields = ('payment_method', 'course',)
    permission_classes = [IsAuthenticated]


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    """отображение одной сущности"""

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()


class PaymentsUpdateAPIView(generics.UpdateAPIView):
    """редактирование сущности"""

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsUserOrStaff]


class PaymentsDestroyAPIView(generics.DestroyAPIView):
    """удаление сущности"""

    queryset = Payments.objects.all()
    permission_classes = [UserIsStaff]

    """Классы на основе generics для PaymentsHistory"""


class PaymentsHistoryCreateAPIView(generics.CreateAPIView):
    """создание сущности"""

    serializer_class = PaymentsHistorySerializer
    permission_classes = [IsAuthenticated]


class PaymentsHistoryListAPIView(generics.ListAPIView):
    """отображение списка сущностей"""

    serializer_class = PaymentsHistorySerializer
    queryset = PaymentsHistory.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentsHistoryRetrieveAPIView(generics.RetrieveAPIView):
    """отображение одной сущности"""

    serializer_class = PaymentsHistorySerializer
    queryset = PaymentsHistory.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentsHistoryUpdateAPIView(generics.UpdateAPIView):
    """редактирование сущности"""

    serializer_class = PaymentsHistorySerializer
    queryset = PaymentsHistory.objects.all()
    permission_classes = [IsUserOrStaff]


class PaymentsHistoryDestroyAPIView(generics.DestroyAPIView):
    """удаление сущности"""

    queryset = Payments.objects.all()
    permission_classes = [UserIsStaff]


class CourseSubscriptionCreateAPIView(generics.CreateAPIView):
    """создание сущности подписки"""

    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer
    permission_classes = [IsAuthenticated]


class CourseSubscriptionDestroyAPIView(generics.DestroyAPIView):
    """удаление сущности подписки"""

    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer
    permission_classes = [IsAuthenticated]
