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


class ProductVariation(models.Model):
    class Meta:
        pass

    product_variation_name = models.CharField(max_length=100)
    product_variation_description = models.TextField(max_length=500, null=True, blank=True)

    product = models.ForeignKey(Product, related_name='product_variation', on_delete=models.PROTECT)


class BarProduct(models.Model):
    class Meta:
        pass

    bar_product_prize = models.IntegerField(default=0)
    bar_product_stock = models.BooleanField(default=False)

    bar_product_combo = models.ManyToManyField(Combo, related_name='bar_product_combo')
    bar_product_order_list = models.ManyToManyField(OrderList, 'bar_product_order_list')




