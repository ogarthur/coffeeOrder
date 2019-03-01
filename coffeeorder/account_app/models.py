from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userInfo")

    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile_pics/avatar.png')
    language = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)

    def __str__(self):
        return self.user.username


class UserGroup(models.Model):

    group_name = models.CharField(max_length=100, unique=True)
    group_description = models.TextField(max_length=220)
    max_members = models.IntegerField(default=15)
    group_pic = models.ImageField(upload_to='group_pics/', default='group_pics/coffee.png',  null=True, blank=True)
    group_code = models.CharField(max_length=100)
    fav = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    group_admin = models.ManyToManyField(User, related_name='groupAdmin')
    group_members = models.ManyToManyField(User, related_name='groupMembers')

    def __str__(self):
        return self.group_name
