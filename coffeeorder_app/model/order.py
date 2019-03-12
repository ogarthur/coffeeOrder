#-*- coding: utf-8 -*-

from django.db import models
from .orderlist import OrderList
from .productbar import ProductBar
from account_app.models import UserGroup
from django.contrib.auth.models import User
from .combo import Combo


class Order(models.Model):
    class Meta:
        pass

    order_id = None

    order_order_list = models.ForeignKey(OrderList, related_name='OrderList', on_delete=models.PROTECT)
    order_product_bar = models.ManyToManyField(ProductBar, related_name='ProductBar')
    order_user = models.ForeignKey(User, related_name='User', on_delete=models.PROTECT)
    order_group = models.ForeignKey(UserGroup, related_name='UserGroup', on_delete=models.PROTECT)
    order_combo = models.ManyToManyField(Combo, related_name='Combo')

