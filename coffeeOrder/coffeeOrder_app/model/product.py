#-*- coding: utf-8 -*-

from django.db import models
from .bar import Bar
from .combo import Combo
from .orderlist import OrderList


class Product(models.Model):
    class Meta:
        pass

    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=500, null=True, blank=True)
    product_logo = models.ImageField(upload_to='product_logos/', default='product.png',)

    bar_product = models.ManyToManyField(Bar, related_name='product_bar')


class ProductBar(models.Model):
    class Meta:
        pass

    product_bar_prize = models.IntegerField(default=0)
    product_bar_stock = models.BooleanField(default=False)

    product_combo = models.ManyToManyField(Combo, related_name='product_combo')
    product_order_list = models.ManyToManyField(OrderList, 'product_order_list')




