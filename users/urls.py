from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('users/create/', UserCreateAPIView.as_view(), name='users-create'),
    path('users/', UserListAPIView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='users-get'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='users-update'),
    path('users/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='users-delete'),
]
