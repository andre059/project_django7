from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    """Урок"""

    title = models.CharField(max_length=150, verbose_name='название урока')
    duration = models.IntegerField(verbose_name='продолжительность урока', **NULLABLE)
    picture = models.ImageField(upload_to='preview_lesson/', verbose_name='предварительный просмотр урока', **NULLABLE)
    link_video = models.TextField(verbose_name='ссылка на видео')

    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Автор')

    def __str__(self):
        return f'{self.title} {self.duration}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Course(models.Model):
    """Курс"""

    title = models.CharField(max_length=150, verbose_name='название курса')
    picture = models.ImageField(upload_to='course_preview/', null=True, verbose_name='предварительный просмотр курса')
    description = models.TextField(verbose_name='описание')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Автор')

    course_price = models.PositiveIntegerField(default=0, verbose_name='Цена курса')
    update_time = models.DateTimeField(auto_now=True, **NULLABLE, verbose_name='Обновление')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
