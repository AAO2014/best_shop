from django.urls import path, include
from rest_framework import routers

from .api import PaymentViewSet

app_name = 'payments'

router = routers.DefaultRouter()
router.register(r'list', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
