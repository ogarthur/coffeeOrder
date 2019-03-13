#-*- coding: utf-8 -*-

from django.db import models
from .bar import Bar
PRODUCT_CHOICES = (
    ('COMIDA', 'comida'),
    ('BEBIDA', 'Bebida'),

)


class Product(models.Model):
    class Meta:
        pass

    product_name = models.CharField(max_length=200, unique=True)
    product_color = models.CharField(max_length=100, default="white")
    product_type = models.CharField(choices=PRODUCT_CHOICES, max_length=50)
    product_bar = models.ManyToManyField(Bar, related_name='product_bar')


class ProductVariation(models.Model):
    class Meta:
        pass

    product_variation_name = models.CharField(max_length=300, default="NONE")

    product_variation_product = models.ForeignKey(Product, related_name='variation_product', on_delete=models.PROTECT)

