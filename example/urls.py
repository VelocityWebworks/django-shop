from django.urls import include, path, re_path
from example.myshop.views import MyOrderConfirmView

from shop import urls as shop_urls
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    path('checkout/confirm/', MyOrderConfirmView.as_view(), name='checkout_shipping'),
    re_path(r'^', include(shop_urls)),  # <-- That's the important bit
]
