from django.db import models
from django.utils.translation import gettext_lazy as _

from goods.models import Good


class Order(models.Model):
    STATUSES = (
        ('created', 'Created order'),
        ('confirmed', 'Confirmed'),
        ('transfer', 'On a way to customer'),
        ('delivered', 'On a way to customer'),
        ('user_canceled', 'Canceled by customer'),
        ('shop_canceled', 'Canceled by shop'),
    )
    total_money = models.FloatField(verbose_name=_('total money'), null=True, blank=True)  # или MoneyField
    status = models.CharField(choices=STATUSES, max_length=20, verbose_name=_('status'), default='created', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created time'), null=True, blank=True)
    completed = models.DateTimeField(verbose_name=_('completion time'), null=True, blank=True)

    def __str__(self):
        return f'{self.created.date()} - {self.total_money}'


class OrderPart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('order'), related_name='order')
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name=_('good'))

    def __str__(self):
        return f'{_("Order")}: {self.order.id}, {_("good")}: {self.good}'
