from datetime import datetime, timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from education.models import Course
from users.models import CourseSubscription, User


@shared_task
def send_updated_email(course_id):
    """Aсинхроннуя рассылка писем пользователям об обновлении материалов курс"""

    course = Course.objects.get(pk=course_id)
    subscription = CourseSubscription.objects.filter(course=course_id)
    update_time = course.update_time

    if timezone.now() - update_time > timezone.timedelta(hours=4):  # Проверка, если курс не обновлялся более 4 часов
        if subscription:
            for signed in subscription:
                send_mail(
                    subject="Обновление курса!",
                    message=f"У курса {course.title} появился новый урок!",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[signed.subscriber]
                )


@shared_task
def check_user():
    """проверка пользователей по дате последнего входа по полю last_login,
    если пользователь не заходил более месяца, блокируется с помощью флага is_active"""

    now = datetime.now()
    month_ago = now - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__gt=month_ago)
    inactive_users.update(is_active=False)

    for user in inactive_users:
        user.is_active = False
        user.save()
        print(f'Пользователь {user.username} заблокирован')
