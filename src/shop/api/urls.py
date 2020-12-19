from .views import ShopCarRUDView, ShopCarAPIView

from django.contrib import admin
from django.urls import path,re_path

urlpatterns = [
    re_path(r'^$', ShopCarAPIView.as_view(), name='car-create'),
    re_path(r'^(?P<pk>\d+)/$', ShopCarRUDView.as_view(), name='car-rud')
]
