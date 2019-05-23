#-*- coding: utf-8 -*-

from django.db import models
from .bar import Bar
from .combo import Combo


PRODUCT_CHOICES = (
    ('0', 'food'),
    ('1', 'drink'),

)


class Product(models.Model):

    class Meta:
        pass

    product_name = models.CharField(max_length=200, unique=True)
    product_color = models.CharField(max_length=100, default="yellow")
    product_type = models.CharField(choices=PRODUCT_CHOICES, max_length=50)

    def __str__(self):
        return self.product_name


class ProductVariation(models.Model):

    class Meta:
        pass

    product_variation_name = models.CharField(max_length=300, default="NONE")
    product_variation_product = models.ForeignKey(Product, related_name='variation_product', on_delete=models.PROTECT)


class ProductBar(models.Model):

    class Meta:
        pass

    product_bar_prize = models.FloatField()
    product_bar_stock = models.BooleanField(default=True)

    #product_bar_combo = models.ManyToManyField(Combo, related_name='Combo')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    product_bar_bar = models.ForeignKey('Bar', on_delete=models.PROTECT)

    def __str__(self):
        return "[{}] {}".format( self.product_bar_bar.bar_name, self.product.product_name)