#-*- coding: utf-8 -*-

from django.db import models
from .combo import  Combo
from .orderlist import OrderList
from .bar import Bar

class ProductBar(models.Model):
    class Meta:
        pass

    product_bar_prize = models.IntegerField()
    product_bar_stock = models.IntegerField(default=0)

    product_bar_combo = models.ManyToManyField(Combo, related_name='Combo')
    product_bar_order = models.ManyToManyField(OrderList, related_name='OrderList')

    product_bar_bar = models.ForeignKey('Bar', on_delete=models.PROTECT)

