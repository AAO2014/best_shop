from django.contrib import admin

from goods.models import Good


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    model = Good
    list_display = ('title', 'picture', 'content', 'price', )
