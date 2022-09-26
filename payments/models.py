from django.db import models
from django.utils.translation import gettext_lazy as _

from orders.models import Order


class Payment(models.Model):
    STATUSES = (
        ('created', 'created'),
        ('paid', 'paid'),
    )
    TYPES = (
        ('instant', 'instant'),
        ('receipt', 'payment upon receipt'),
    )
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name=_('order'))
    amount = models.FloatField(verbose_name=_('Money amount'))  # или MoneyField
    status = models.CharField(choices=STATUSES, max_length=20, verbose_name=_('status'), default='created')
    type = models.CharField(choices=TYPES, max_length=20, verbose_name=_('type'), default='instant')

    def __str__(self):
        return f'{self.amount}'
