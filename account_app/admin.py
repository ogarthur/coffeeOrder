from django.contrib import admin

# Register your model here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your model here.
from .models import CustomUser, UserGroup
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your model here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register( UserGroup)


