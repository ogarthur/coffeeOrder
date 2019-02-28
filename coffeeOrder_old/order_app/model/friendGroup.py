#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class FriendGroup(models.Model):
    class Meta:
        pass

    group_name = models.CharField(max_length=100)
    group_description = models.TextField(max_length=500, null=True, blank=True)
    group_logo = models.ImageField(upload_to='group_logos/', default='group.png',)

    members = models.ManyToManyField(User, related_name='member_user')


    def __str__(self):
        return 'id:{}, grupo:{}'.format(self.pk, self.group_name)
