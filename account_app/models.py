from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
PROFILE_PIC_CHOICES = (
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

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userInfo")

    profile_pic = models.CharField(choices=PROFILE_PIC_CHOICES, default='0', max_length=100 )
    language = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)

    def __str__(self):
        return self.user.username


class UserGroup(models.Model):

    group_name = models.CharField(max_length=100, unique=True)
    group_description = models.TextField(max_length=220, blank=True)
    max_members = models.IntegerField(default=15)
    group_color = models.CharField(max_length=100, default="white")
    group_code = models.CharField(max_length=100)
    closed = models.BooleanField(default=False)
    group_admin = models.ManyToManyField(User, related_name='groupAdmin')
    group_members = models.ManyToManyField(User, related_name='groupMembers')

    def __str__(self):
        return self.group_name
