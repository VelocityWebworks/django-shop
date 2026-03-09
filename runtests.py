#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings

if not settings.configured:
    directory = os.path.abspath("%s" % os.path.dirname(__file__))

    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "test.sqlite",
            },
        },
        INSTALLED_APPS=(
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.sites",
            "django.contrib.messages",
            "django.contrib.admin",
            "polymorphic",
            "shop",
            "shop.addressmodel",
            "project",
        ),
        MIDDLEWARE=(
            "django.middleware.common.CommonMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
        ),
        ROOT_URLCONF="testapp.urls",
        SITE_ID=1,
        STATIC_URL="%s/testapp/static/" % directory,
        STATIC_ROOT="static/",
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [],
                "APP_DIRS": True,
                "OPTIONS": {
                    "context_processors": [
                        "django.contrib.auth.context_processors.auth",
                        "django.template.context_processors.debug",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.media",
                        "django.template.context_processors.static",
                        "django.contrib.messages.context_processors.messages",
                        "django.template.context_processors.request",
                    ],
                },
            }
        ],
        PASSWORD_HASHERS=("django.contrib.auth.hashers.MD5PasswordHasher",),
        DEFAULT_AUTO_FIELD="django.db.models.AutoField",
        # The shop settings:
        SHOP_CART_MODIFIERS=["shop.cart.modifiers.rebate_modifiers.BulkRebateModifier"],
        SHOP_SHIPPING_BACKENDS=["shop.shipping.backends.flat_rate.FlatRateShipping"],
        SHOP_PAYMENT_BACKENDS=[
            "shop.payment.backends.pay_on_delivery.PayOnDeliveryBackend"
        ],
        SHOP_SHIPPING_FLAT_RATE="10",
        SECRET_KEY="test1234",
    )


def run_django_tests():
    django.setup()
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    apps = ["shop", "shop.addressmodel"]
    failures = test_runner.run_tests(apps)
    sys.exit(failures)


if __name__ == "__main__":
    run_django_tests()
