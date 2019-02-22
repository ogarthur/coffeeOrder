#-*- coding: utf-8 -*-

from django.db import models

class Bar(models.Model):
    class Meta:
        pass

    bar_name = undefined()
    bar_logo = undefined()

     = models.OneToOne('Combo')

