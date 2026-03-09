# -*- coding: utf-8 -*-
from django.urls import include, re_path

from shop.views import ShopTemplateView


urlpatterns = [
    re_path(r'^$', ShopTemplateView.as_view(template_name="shop/welcome.html"),
        name='shop_welcome'),
    re_path(r'^pay/', include('shop.payment.urls')),
    re_path(r'^ship/', include('shop.shipping.urls')),
    re_path(r'^orders/', include('shop.urls.order')),
    re_path(r'^checkout/', include('shop.urls.checkout')),
    re_path(r'^cart/', include('shop.urls.cart')),
    re_path(r'^products/', include('shop.urls.catalog')),
]
