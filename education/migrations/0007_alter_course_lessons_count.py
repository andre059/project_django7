# Generated by Django 4.2.7 on 2023-11-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_alter_course_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lessons_count',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='количество уроков'),
        ),
    ]
