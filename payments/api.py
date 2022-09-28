from rest_framework import viewsets, status
from rest_framework.response import Response

from best_shop.api_const import INSTANCE_DOES_NOT_EXISTS
from orders.models import Order
from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a payment instance

        Required keys: order id value (int type)
        Optional keys: status and type (please see Payment model for valid values)
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order.objects.filter(id=request.data['order'])
        if not order.exists():
            raise ValueError(INSTANCE_DOES_NOT_EXISTS)
        money = order.first().total_money
        payment = Payment.objects.create(**serializer.data, order_id=serializer.initial_data['order'], amount=money, )
        headers = self.get_success_headers(serializer.data)
        return Response(data={'payment_id': payment.id}, status=status.HTTP_201_CREATED, headers=headers)
