from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext as _
from .models import UserGroup, CustomUser
from django.core.files.images import get_image_dimensions


class CustomUserCreationForm(UserCreationForm):
    """ Clase formulario para datos de usuarios basicos"""
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', }))

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in [ 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget = forms.PasswordInput(attrs={'class': 'form-control', })

    class Meta(UserCreationForm):
        model = CustomUser
        msg_required = "Obligatory field"
        fields = (
            'username',
            'first_name',
            'email',
            'password1',
            'password2',
            'profile_pic',
        )
        fields_required = (
            'username',
            'email',
            'password1',
            'password2',
        )

        labels = {
            'username': _('UserName'),
            'first_name': _('Name'),
            'email': _('Email:'),
            'profile_pic': _('Profile avatar:'),
        }
        help_texts = {
            'first_name': _('Not obligatory, just to identify easily the user'),
            'password1': _('not needed'),
            'password2': "SS",
        }
        error_messages = {
            'username': {
                'max_length': _("Length not valid"),
                'required': _(msg_required)
            },

            'email': {
                'required': _(msg_required)
            },
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', }),
            'first_name': forms.TextInput(attrs={'class': 'form-control', }),
            'email': forms.EmailInput(attrs={'class': 'form-control', }),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', }),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', }),
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name')


class UserForm(forms.ModelForm):
    """ Clase formulario para datos de usuarios basicos"""
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control ', }))

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            msg = "Passwords do not match"
            self.add_error('password', msg)

    class Meta:
        model = User
        msg_required = "Obligatory field"
        fields = (
        'username',
        'first_name',
        'email',
        'password',
        'confirm_password'
        )
        fields_required= (
            'username',
            'email',
            'password',
            'confirm_password'
            )

        labels = {
            'username': _('UserName'),
            'first_name': _('Name'),
            'email': _('Email:'),
            'password':  _('Password :'),
            'confirm_password':    _('Confirm password:'),
        }
        help_texts = {
            'first_name': _('Not obligatory, just to identify easily the user'),
        }
        error_messages = {
            'username': {
                'max_length': _("Length not valid"),
                'required': _(msg_required)
            },
            'password': {
                'required': _(msg_required)
            },
            'confirm_password': {
                'required': _(msg_required)
            },
            'email': {
                'required': _(msg_required)
            },
        }
        widgets = {
                    'username': forms.TextInput(attrs={'class': 'form-control',}),
                    'first_name': forms.TextInput(attrs={'class': 'form-control',}),
                    'email': forms.EmailInput(attrs={'class': 'form-control',}),
                }

'''
class UserProfileForm(forms.ModelForm):
    """ Clase formulario detalles adicionales sobre el usuario"""

    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
        labels = {
                'profile_pic': _('Profile avatar:'),
                }
        help_texts = {
        }
        widgets = {
        }
'''

class GroupForm(forms.ModelForm):
    """ FORMULARIO PARA CREAR GRUPOS"""

    class Meta:
        model = UserGroup
        fields = ('group_name', 'group_description', 'max_members', 'group_color', )
        labels = {
                'group_name': _('Name of the group'),
                'group_description': _('Describe  the group'),
                'max_members': _('Max number of members'),
                'group_color': _('Group color'),
                }
        help_texts = {

        }
        widgets = {
            'group_name': forms.TextInput(attrs={'class': 'form-control', }),
            'group_description': forms.TextInput(attrs={'class': 'form-control', }),
            'max_members': forms.NumberInput(attrs={'class': 'form-control', }),
            'group_color':  forms.TextInput(attrs={'class': 'form-control color-menu', }),
        }
class JoinGroupForm(forms.Form):
    """ FORMULARIO PARA CREAR GRUPOS"""

    group_code = forms.CharField(label='Invitation code', widget=forms.TextInput(attrs={'required': 'required', 'class': 'form-control', }))

    def clean(self):
        all_clean_data = super( JoinGroupForm, self).clean()
        group_code = all_clean_data['group_code']