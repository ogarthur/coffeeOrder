#-*- coding: utf-8 -*-

from django.db import models

from account_app.models import UserGroup
from django.contrib.auth.models import User
from .combo import Combo
from ..model.product import ProductBar
from datetime import datetime, timedelta
from .bar import Bar

class OrderList(models.Model):

    class Meta:
        pass

    created = models.DateTimeField(blank=True)
    expiration = models.DateTimeField(blank=True)

    total_prize = models.IntegerField(default=0)

    order_bar = models.ForeignKey(Bar, related_name='Bar', on_delete=models.PROTECT)
    order_group = models.ForeignKey(UserGroup, related_name='UserGroup', on_delete=models.PROTECT)

class Order(models.Model):
    class Meta:
        pass

    order_id = None

    order_order_list = models.ForeignKey(OrderList, related_name='OrderList', on_delete=models.PROTECT)
    order_product_bar = models.ManyToManyField(ProductBar, related_name='ProductBar')
    #order_user = models.ForeignKey(User, related_name='orderUser', on_delete=models.PROTECT)
    order_group = models.ForeignKey(UserGroup, related_name='orderUserGroup', on_delete=models.PROTECT)
    order_combo = models.ManyToManyField(Combo, related_name='orderCombo')



