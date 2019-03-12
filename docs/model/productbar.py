#-*- coding: utf-8 -*-

from django.db import models

class ProductBar(models.Model):
    class Meta:
        pass

    product_bar_prize = undefined()
    product_bar_stock = undefined()

     = models.ManyToMany('Combo')
     = models.ManyToMany('OrderList')
     = models.ForeignKey('Bar', on_delete=models.PROTECT)
     = models.ManyToMany('Combo')
     = models.ManyToMany('Order')

