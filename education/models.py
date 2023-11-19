from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    """Курс"""
    title = models.CharField(max_length=150, verbose_name='название курса')
    picture = models.ImageField(upload_to='course_preview/', verbose_name='предварительный просмотр курса', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    lessons_count = models.IntegerField(null=True, verbose_name='количество уроков')

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

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
