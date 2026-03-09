from django.urls import re_path
from shop.views.product import (ProductListView, ProductDetailView)


urlpatterns = [
    re_path(
        r'^$',
        ProductListView.as_view(),
        name='product_list'
    ),
    re_path(
        r'^(?P<slug>[0-9A-Za-z-_.//]+)/$',
        ProductDetailView.as_view(),
        name='product_detail'
    ),
]
