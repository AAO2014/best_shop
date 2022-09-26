from django.db import models
from django.utils.translation import gettext_lazy as _

from best_shop.settings import UPLOAD_ROOT


class Good(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    picture = models.ImageField(upload_to=f'{UPLOAD_ROOT}/good_pics/%Y/%m/%d/', verbose_name=_('picture'), null=True,
                                blank=True)
    content = models.TextField(verbose_name=_('content'))
    price = models.FloatField(verbose_name=_('price'))  # можно использовать специализированное поле вроде MoneyField

    def __str__(self):
        return self.title
