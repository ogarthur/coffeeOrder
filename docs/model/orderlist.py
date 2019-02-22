#-*- coding: utf-8 -*-

from django.db import models

class OrderList(models.Model):
    class Meta:
        pass

    created = undefined()
    total_prize = undefined()

     = models.ForeignKey('Bar', on_delete=models.PROTECT)
     = models.ManyToMany('Combo')

