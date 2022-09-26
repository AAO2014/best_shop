from django.contrib import admin
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from orders.models import Order, OrderPart


def confirm(modeladmin, request, queryset):
    for order in queryset:
        if order.payment.status == 'paid':
            order.status = 'confirmed'
            order.completed = now()
            order.save()
confirm.short_description = _("Confirm orders")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('id', 'total_money', 'status', 'created', 'completed', )
    actions = [confirm, ]


@admin.register(OrderPart)
class OrderPartAdmin(admin.ModelAdmin):
    model = OrderPart
