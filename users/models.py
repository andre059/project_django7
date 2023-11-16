from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Курс"""
    title = models.CharField(max_length=150, verbose_name='название курса')
    picture = models.ImageField(upload_to='course_preview/', verbose_name='предварительный просмотр курса', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """Урок"""
    title = models.CharField(max_length=150, verbose_name='название курса')
    description = models.TextField(verbose_name='описание')
    picture = models.ImageField(upload_to='preview_lesson/', verbose_name='предварительный урок', **NULLABLE)
    link_video = models.TextField(verbose_name='ссылка на видео')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class User(AbstractUser):
    """Пользователь"""

    username = None

    surname = models.CharField(max_length=150, null=True, verbose_name='фамилия')
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активный')
    date_of_birth = models.DateField(verbose_name='дата_рождения', **NULLABLE)

    courses = models.ManyToManyField(Course, related_name='users', verbose_name='курсы')
    lessons = models.ManyToManyField(Lesson, related_name='users', verbose_name='уроки')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def has_perm(self, perm, obj=None):
        """Есть ли у пользователя определенное разрешение?"""
        return True


class EmailVerificationToken(models.Model):
    """
    Модель предназначена для хранения информации о токене верификации электронной почты пользователя.
    Она связана с конкретным пользователем через внешний ключ user,
    хранит сам токен token и дату его создания created_at.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь')

    token = models.CharField(max_length=255, unique=True, verbose_name='токен верификации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания токена')

    def __str__(self):
        return f'{self.token} {self.created_at}'
