#-*- coding: utf-8 -*-

from django.db import models

class Product(models.Model):
    class Meta:
        pass

    product_name = undefined()
    product_description = undefined()
    Product_logo = undefined()

     = models.ManyToMany('Bar')

