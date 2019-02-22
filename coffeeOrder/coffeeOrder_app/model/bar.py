#-*- coding: utf-8 -*-

from django.db import models
from .combo import Combo


class Bar(models.Model):
    class Meta:
        pass

    bar_name = models.CharField(max_length=100)
    bar_logo = models.ImageField(upload_to='bar_logos/', default='bar.png',)

    bar_combo = models.OneToOneField(Combo, related_name='bar_combo', on_delete=models.CASCADE, null=True)

