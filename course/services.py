import stripe
from course.models import Payments
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def get_session_with_pay(serializer: Payments):
    course_title = serializer.paid_course.title
    product = stripe.Product.create(name=course_title)
    price = stripe.Price.create(
        product=product.id,
        unit_amount=serializer.payment_amount * 100,
        currency='usd',
    )
    session = stripe.checkout.Session.create(
        success_url='https://example.com/success',
        line_items=[
            {
                'price': price.id,
                'quantity': 1,
            }
        ],
        mode='payment',
    )
    print(session.url)
    return session
