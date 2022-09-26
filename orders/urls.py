from django.urls import path, include, reverse
from rest_framework import routers

from orders.api import OrderViewSet, OrderPartViewSet

app_name = 'orders'

router = routers.DefaultRouter()
router.register(r'list', OrderViewSet)
router.register(r'part', OrderPartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
