#-*- coding: utf-8 -*-

from django.db import models

class User(models.Model):
    class Meta:
        pass

    user_id = undefined()

     = models.ManyToMany('Group')
     = models.ManyToMany('OrderList')

