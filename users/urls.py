from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsCreateAPIView, PaymentsListAPIView, PaymentsRetrieveAPIView, \
    PaymentsUpdateAPIView, PaymentsDestroyAPIView, PaymentsHistoryCreateAPIView, PaymentsHistoryListAPIView, \
    PaymentsHistoryRetrieveAPIView, PaymentsHistoryUpdateAPIView, PaymentsHistoryDestroyAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'lesson', UserViewSet, basename='lesson')

urlpatterns = [
    # Payments
    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments-create'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
    path('payments/<int:pk>/', PaymentsRetrieveAPIView.as_view(), name='payments-get'),
    path('payments/update/<int:pk>/', PaymentsUpdateAPIView.as_view(), name='payments-update'),
    path('payments/delete/<int:pk>/', PaymentsDestroyAPIView.as_view(), name='payments-delete'),

    # PaymentsHistory
    path('paymentsHistory/create/', PaymentsHistoryCreateAPIView.as_view(), name='paymentsHistory-create'),
    path('paymentsHistory/', PaymentsHistoryListAPIView.as_view(), name='paymentsHistory-list'),
    path('paymentsHistory/<int:pk>/', PaymentsHistoryRetrieveAPIView.as_view(), name='paymentsHistory-get'),
    path('paymentsHistory/update/<int:pk>/', PaymentsHistoryUpdateAPIView.as_view(), name='paymentsHistory-update'),
    path('paymentsHistory/delete/<int:pk>/', PaymentsHistoryDestroyAPIView.as_view(), name='paymentsHistory-delete'),
] + router.urls
