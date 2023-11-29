# Generated by Django 4.2.7 on 2023-11-29 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0012_course_author_course_price_course_update_time_and_more'),
        ('users', '0008_coursesubscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursesubscription',
            name='subscription',
        ),
        migrations.AddField(
            model_name='coursesubscription',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Статус подписки'),
        ),
        migrations.AddField(
            model_name='coursesubscription',
            name='subscriptions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='подписки'),
        ),
        migrations.AddField(
            model_name='payments',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.lesson', verbose_name='Урок'),
        ),
        migrations.AddField(
            model_name='payments',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Stripe ID'),
        ),
        migrations.AddField(
            model_name='payments',
            name='stripe_status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Stripe статус'),
        ),
        migrations.AlterField(
            model_name='coursesubscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Наличные'), ('transfer', 'Перевод на счет')], default='transfer', max_length=150, verbose_name='способ оплаты'),
        ),
    ]
