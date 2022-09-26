import requests
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

from best_shop.api_const import ORDER_PARTS_API_KEY, CONFIRMED_ORDER_URL
from goods.models import Good
from orders.models import Order, OrderPart
from orders.serializers import OrderSerializer, OrderPartSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates an order instance

        Required keys: OrderPart id list (element type - int), see ORDER_PARTS_API_KEY constant
        Optional keys: status, created and completed (please see Order model for valid values)
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        goods = Good.objects.filter(id__in=request.data[ORDER_PARTS_API_KEY])
        total_money = goods.aggregate(total=Sum('price'))['total']
        new_order = Order.objects.create(**serializer.data, total_money=total_money)
        for good in Good.objects.filter(id__in=goods):
            OrderPart.objects.create(order=new_order, good=good)
        headers = self.get_success_headers(serializer.data)
        return Response('OK', status=status.HTTP_201_CREATED, headers=headers)


class OrderPartViewSet(viewsets.ModelViewSet):
    queryset = OrderPart.objects.all()
    serializer_class = OrderPartSerializer


@csrf_exempt
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_confirmed(request, pk):
    order = Order.objects.get(id=pk)
    if order.payment.status == 'paid':
        order.status = 'confirmed'
        order.completed = now()
        order.save()
        requests.post(
            CONFIRMED_ORDER_URL,
            {"id": pk, "amount": order.total_money, "date": order.completed}
        )
    return redirect(reverse('admin:orders_order_change', kwargs={'object_id': pk}))
