from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from best_shop.api_const import ORDER_API_KEY, PAYMENT_ALREADY_EXISTS_MESSAGE
from .models import Payment


class PaymentSerializer(serializers.Serializer):
    order = serializers.PrimaryKeyRelatedField(label=_('order'), read_only=True)
    amount = serializers.FloatField(label=_('amount'), required=False)
    status = serializers.CharField(label=_('status'), required=False)
    type = serializers.DateTimeField(label=_('type'), required=False)

    class Meta:
        model = Payment
        fields = ('amount', 'status', 'type', )

    def error_handling(self, message, raise_exception):
        if raise_exception:
            raise ValueError(f'{ORDER_API_KEY} {message}!')
        else:
            self._errors[ORDER_API_KEY] = f'{message}!'
            return False

    def is_valid(self, raise_exception=False):
        result = super().is_valid(raise_exception)
        if Payment.objects.filter(order=self.initial_data['order']).exists():
            result = self.error_handling(PAYMENT_ALREADY_EXISTS_MESSAGE, raise_exception)
        return result
