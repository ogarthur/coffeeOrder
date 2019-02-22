#-*- coding: utf-8 -*-

from django.db import models
from .bar import Bar
from .combo import Combo
from django.contrib.auth.models import User

class OrderList(models.Model):
    class Meta:
        pass

    created = models.DateField(null=True)
    total_prize = models.DecimalField(default='0.00', max_digits=5, decimal_places=2)
    order_state = models.BooleanField(default=False)

    order_bar = models.ForeignKey(Bar, related_name='order_bar', on_delete=models.PROTECT)
    bar_combo = models.ManyToManyField(Combo, related_name='order_combo')

    order_members = models.ManyToManyField(User, related_name='order_member_user')

