from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from goods.models import Good


class GoodSerializer(serializers.Serializer):
    title = serializers.CharField(label=_('title'))
    picture = serializers.ImageField(label=_('picture'))
    content = serializers.CharField(label=_('content'))
    price = serializers.FloatField(label=_('price'))

    class Meta:
        model = Good
        fields = ('title', 'picture', 'content', 'price')
