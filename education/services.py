import json
import os
from datetime import datetime, timedelta

import requests
import stripe
from django.conf import settings
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from rest_framework import status

from education.models import Course
from users.models import Payments

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


def convert_currencies(rub_prise):
    usd_price = 0
    response = requests.get(
        f'{settings.CUR_API_URL}https://api.currencyapi.com/v3/latest?apikey={settings.CUR_API_KEY}&currencies=RUB'
    )
    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['data']['RUB']['value']
        usd_price = rub_prise * usd_rate
    return usd_price


def create_stripe_checkout_session(course_id):
    course = Course.objects.get(pk=course_id)

    product = stripe.Product.create(
        name=course.title,
        description="$100/Month subscription",
        type="service",
    )

    price = stripe.Price.create(
        unit_amount=course.price,
        currency="usd",
        product=product.get('id'),
        stripe_account='STRIPE_SECRET_KEY',
    )

    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            },
        ],
        mode="payment",
    )

    return session


def get_stripe_payment(pk):
    payment = Payments.objects.get(pk=pk)

    payment_detail = stripe.checkout.Session.retrieve(
        payment.stripe_id,
    )

    return payment_detail


def set_schedule(*args, **kwargs):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS,
    )
    PeriodicTask.objects.create(
        interval=schedule,
        name='Importing contacts',
        task='proj.tasks.import_contacts',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
