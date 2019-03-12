#-*- coding: utf-8 -*-

from django.db import models

class Group(models.Model):
    class Meta:
        pass

    group_name = undefined()
    group_logo = undefined()

     = models.ManyToMany('Bar')

