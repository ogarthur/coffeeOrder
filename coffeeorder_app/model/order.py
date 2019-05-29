#-*- coding: utf-8 -*-

from django.db import models

from account_app.models import UserGroup
from .combo import Combo
from ..model.product import ProductBar
from datetime import datetime, timedelta
from .bar import Bar
from account_app.models import CustomUser
from django.db.models import Q


class OrderList(models.Model):
    """
     Represents the list of orders of a a group.
    """
    class Meta:
        pass

    created = models.DateTimeField(blank=True)
    user_creator = models.ForeignKey(CustomUser, related_name='orderListCreator', on_delete=models.PROTECT)
    expiration = models.DateTimeField(blank=True)
    total_prize = models.IntegerField(default=0)
    order_bar = models.ForeignKey(Bar, related_name='Bar', on_delete=models.PROTECT)
    order_group = models.ForeignKey(UserGroup, related_name='UserGroup', on_delete=models.PROTECT)
    state = models.BooleanField(default=True)

    def check_state(self):
        """
        Function to check if the order_list should be still active
        :return: True if it should be still active
        """
        today = datetime.today()
        orders = OrderList.objects.filter(Q(expiration__lte=today))
        for order in orders:
            order.state = False
            order.save()

    def __str__(self):
        return "ORDER_LIST:{}-{}".format(self.pk, self.order_group_id)


class Order(models.Model):
    class Meta:
        pass

    order_order_list = models.ForeignKey(OrderList, related_name='OrderList', on_delete=models.CASCADE)
    order_user = models.ForeignKey(CustomUser, related_name='orderUser', on_delete=models.CASCADE)

    def __str__(self):
        return "ORDER:{}_{}_{}".format(self.order_order_list.pk, self.pk, self.order_user.username)


class OrderItem(models.Model):

    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, related_name='ProductOrder', on_delete=models.CASCADE)
    order_product_bar = models.ForeignKey(ProductBar, related_name='OrderProductBar', on_delete=models.CASCADE)

    def __str__(self):
        return "ORDER:{}".format(self.quantity)
