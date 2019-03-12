#-*- coding: utf-8 -*-

from django.db import models

class Product_variation(models.Model):
    class Meta:
        pass

    product_variation_name = undefined()
    product_variation_description = undefined()

     = models.ForeignKey('Product', on_delete=models.PROTECT)

