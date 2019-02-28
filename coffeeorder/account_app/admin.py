from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import UserProfileInfo, UserGroup
# Register your models here.

admin.site.register([UserProfileInfo, UserGroup])


