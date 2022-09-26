from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from best_shop.api_const import ORDER_PARTS_API_KEY, KEY_DOES_NOT_EXIST_MESSAGE, VALUE_HAS_NOT_INTEGER_ELEMENTS_MESSAGE
from orders.models import Order, OrderPart


class OrderSerializer(serializers.Serializer):
    total_money = serializers.FloatField(label=_('total money'), required=False)
    status = serializers.CharField(label=_('status'), required=False)
    created = serializers.DateTimeField(label=_('created time'), required=False)
    completed = serializers.DateTimeField(label=_('completion time'), required=False)

    class Meta:
        model = Order
        fields = ('total_money', 'status', 'created', 'completed')

    def error_handling(self, message, raise_exception):
        if raise_exception:
            raise ValueError(f'{ORDER_PARTS_API_KEY} {message}!')
        else:
            self._errors[ORDER_PARTS_API_KEY] = f'{message}!'
            return False

    def is_valid(self, raise_exception=False):
        result = super().is_valid(raise_exception)
        if ORDER_PARTS_API_KEY not in self.initial_data:
            result = self.error_handling(KEY_DOES_NOT_EXIST_MESSAGE, raise_exception)
        elif not all([type(i) is int for i in self.initial_data[ORDER_PARTS_API_KEY]]):
            result = self.error_handling(VALUE_HAS_NOT_INTEGER_ELEMENTS_MESSAGE, raise_exception)
        return result


class OrderPartSerializer(serializers.Serializer):
    order = serializers.PrimaryKeyRelatedField(label=_('order'), read_only=True)
    good = serializers.PrimaryKeyRelatedField(label=_('good'), read_only=True)

    class Meta:
        model = OrderPart
        fields = ('order', 'good',)
