from django.urls import re_path
from shop.util.decorators import cart_required

from shop.views.checkout import (
    CheckoutSelectionView,
    PaymentBackendRedirectView,
    ShippingBackendRedirectView,
    OrderConfirmView,
    ThankYouView,
)

urlpatterns = [
    re_path(
        r'^$', cart_required(CheckoutSelectionView.as_view()),
        name='checkout_selection'  # first step of the checkout process
    ),
    re_path(
        r'^ship/$', ShippingBackendRedirectView.as_view(),
        name='checkout_shipping'  # second step of the checkout process
    ),
    re_path(
        r'^confirm/$', OrderConfirmView.as_view(),
        name='checkout_confirm'  # third step of the checkout process
    ),
    re_path(
        r'^pay/$', PaymentBackendRedirectView.as_view(),
        name='checkout_payment'  # fourth step of the checkout process
    ),
    re_path(
        r'^thank_you/$', ThankYouView.as_view(),
        name='thank_you_for_your_order'  # final step of the checkout process
    ),
]
