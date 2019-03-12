#-*- coding: utf-8 -*-

from django.db import models

class Order(models.Model):
    class Meta:
        pass

    order_id = None

     = models.ForeignKey('OrderList', on_delete=models.PROTECT)
     = models.ManyToMany('ProductBar')
     = models.OneToOne('Group')
     = models.ManyToMany('Combo')

