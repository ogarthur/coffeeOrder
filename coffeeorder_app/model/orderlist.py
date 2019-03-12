#-*- coding: utf-8 -*-

from django.db import models
from datetime import datetime, timedelta
from .bar import Bar
from .combo import Combo

class OrderList(models.Model):

    class Meta:
        pass
    # time_created = datetime.datetime.today()
    #time_expiration = time_created + timedelta(hours=2)
    created = models.DateField(blank=True)
    expiration = models.DateField(blank=True)

    total_prize = models.IntegerField()

    order_bar = models.ForeignKey(Bar, related_name='Bar', on_delete=models.PROTECT)


