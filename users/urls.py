from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('users/create/', UserCreateAPIView.as_view(), name='users-create'),
]
