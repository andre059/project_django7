# Generated by Django 4.2.7 on 2023-11-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_emailverificationtoken_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150, verbose_name='пользователь')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')),
                ('course_paid', models.BooleanField(default=False, verbose_name='оплаченный курс')),
                ('payment_amount', models.IntegerField(verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(max_length=150, verbose_name='способ оплаты')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]
