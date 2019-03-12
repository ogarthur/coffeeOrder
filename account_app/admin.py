from django.contrib import admin

# Register your model here.
from django.contrib import admin

# Register your model here.
from .models import UserProfileInfo, UserGroup
# Register your model here.

admin.site.register([UserProfileInfo, UserGroup])


