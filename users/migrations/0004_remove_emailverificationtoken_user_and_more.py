# Generated by Django 4.2.7 on 2023-11-17 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailverificationtoken',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.RemoveField(
            model_name='user',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lessons',
        ),
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='EmailVerificationToken',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
    ]
