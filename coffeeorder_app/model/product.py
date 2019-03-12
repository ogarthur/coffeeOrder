#-*- coding: utf-8 -*-

from django.db import models
from .bar import Bar
PRODUCT_ICON_CHOICES = (
    ('256_0.png', '0'),
    ('256_1.png', '1'),
    ('256_2.png', '2'),
    ('256_3.png', '3'),
    ('256_4.png', '4'),
    ('256_5.png', '5'),
    ('256_6.png', '6'),
    ('256_7.png', '7'),
    ('256_8.png', '8'),
    ('256_9.png', '9'),
    ('256_10.png', '10'),
    ('256_11.png', '11'),
    ('256_12.png', '12'),
    ('256_13.png', '13'),
    ('256_14.png', '14'),
    ('256_15.png', '15'),
    ('256_16.png', '16'),
)


class Product(models.Model):
    class Meta:
        pass

    product_name = models.CharField(max_length=100,unique=True)
    product_description = models.TextField(max_length=500, null=True, blank=True)
    product_icon = models.CharField(choices=PRODUCT_ICON_CHOICES, default='0', max_length=100 )

    product_bar = models.ManyToManyField(Bar, related_name='bar')


