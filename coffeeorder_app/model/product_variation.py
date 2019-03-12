#-*- coding: utf-8 -*-

from django.db import models
from .product import Product


class Product_variation(models.Model):
    class Meta:
        pass

    product_variation_name = models.CharField(max_length=100)
    product_variation_description = models.TextField(max_length=300, blank=True)

    product_variation_product = models.ForeignKey(Product, 'Product', on_delete=models.PROTECT)

