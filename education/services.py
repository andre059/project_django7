import os

import requests
import stripe
from django.conf import settings
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

    starter_subscription = stripe.Product.create(
        name=course,
        description="$100/Month subscription",
    )

    starter_subscription_price = stripe.Price.create(
        unit_amount=course.course_price,
        currency="usd",
        product=starter_subscription['id'],
    )

    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": starter_subscription_price.id,
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
