from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from education.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Пользователь"""

    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активный')
    date_of_birth = models.DateField(verbose_name='дата_рождения', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payments(models.Model):
    """Платежи"""

    CASH = 'cash'
    TRANSFER = 'transfer'

    METHOD_CHOICES = [
        (CASH, 'Наличные'),
        (TRANSFER, 'Перевод на счет')
    ]

    CURRENCY = [
        ('usd', 'USD'),
        ('eur', 'EURO')
    ]

    email = models.EmailField(unique=True, null=True, verbose_name='почта')
    first_name = models.CharField(max_length=150, null=True, verbose_name='имя пользователя')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    course_paid = models.BooleanField(default=False, verbose_name='оплаченный курс')
    payment_amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=150, verbose_name='способ оплаты', default='transfer', choices=METHOD_CHOICES)
    currency = models.CharField(choices=CURRENCY, verbose_name='валюта', default='usd')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок', **NULLABLE)

    stripe_id = models.CharField(max_length=100, verbose_name='Stripe ID', **NULLABLE)
    stripe_status = models.CharField(max_length=50, verbose_name='Stripe статус', **NULLABLE)

    def __str__(self):
        return f'{self.user} {self.payment_date} {self.payment_amount}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'


class PaymentsHistory(models.Model):
    """История платежей"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payments = models.ForeignKey(Payments, on_delete=models.CASCADE, verbose_name='платежи')

    start_payments = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='начало платежей')
    stop_payments = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='конец платежей')

    def __str__(self):
        return f'{self.user} {self.start_payments}--{self.stop_payments}'

    class Meta:
        verbose_name = 'история'
        verbose_name_plural = 'истории'


class CourseSubscription(models.Model):
    """Подписки"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='course_subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    status = models.BooleanField(default=True, verbose_name='Статус подписки')

    subscriptions = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='подписки')

    def __str__(self):
        return f'{self.user} подписка на: {self.course}--{self.status}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписка'
