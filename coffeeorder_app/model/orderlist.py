#-*- coding: utf-8 -*-

from django.db import models
from datetime import datetime, timedelta
from .bar import Bar
from account_app.models import UserGroup
from .combo import Combo


class OrderList(models.Model):

    class Meta:
        pass

    created = models.DateTimeField(blank=True)
    expiration = models.DateTimeField(blank=True)

    total_prize = models.IntegerField(default=0)

    order_bar = models.ForeignKey(Bar, related_name='Bar', on_delete=models.PROTECT)
    order_group = models.ForeignKey(UserGroup, related_name='UserGroup', on_delete=models.PROTECT)

