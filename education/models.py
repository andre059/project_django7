from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    """Урок"""
    title = models.CharField(max_length=150, verbose_name='название урока')
    duration = models.IntegerField(verbose_name='продолжительность урока', **NULLABLE)
    picture = models.ImageField(upload_to='preview_lesson/', verbose_name='предварительный просмотр урока', **NULLABLE)
    link_video = models.TextField(verbose_name='ссылка на видео')

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

    lessons = models.ManyToManyField(Lesson, blank=True, related_name='course', verbose_name='урок')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
