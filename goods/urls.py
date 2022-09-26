from django.urls import path, include
from rest_framework import routers

from goods.api import GoodViewSet

app_name = 'goods'

router = routers.DefaultRouter()
router.register(r'list', GoodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]