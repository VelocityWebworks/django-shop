# Django settings for test project.

DEBUG = True

ADMINS = (,)

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "test.sqlite",
    }
}

TIME_ZONE = "Europe/Zurich"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_TZ = True

SECRET_KEY = "h2%uf!luks79rw^4!5%q#v2znc87g_)@^jf1og!04@&&tsf7*9"

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "testapp.urls"

TEMPLATES = [
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
]

INSTALLED_APPS = (
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
)

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# The shop settings:
SHOP_CART_MODIFIERS = ["shop.cart.modifiers.rebate_modifiers.BulkRebateModifier"]
SHOP_SHIPPING_BACKENDS = ["shop.shipping.backends.flat_rate.FlatRateShipping"]
SHOP_PAYMENT_BACKENDS = ["shop.payment.backends.pay_on_delivery.PayOnDeliveryBackend"]

# Shop module settings
SHOP_SHIPPING_FLAT_RATE = "10"
SECRET_KEY = "test1234"
