from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from .models import UserProfileInfo, UserGroup
from django.core.files.images import get_image_dimensions


class UserForm(forms.ModelForm):
    """ Clase formulario para datos de usuarios basicos"""
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control ',}))

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            msg = "Las contraseñas no coinciden"
            self.add_error('password', msg)

    class Meta():
        model = User
        msg_required = "Campo obligatorio"
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
            'username': _('Nombre de usuario :'),
            'first_name': _('Nombre :'),
            'email': _('Email:'),
            'password':  _('Contraseña :'),
            'confirm_password':    _('Repita contraseña :'),
        }
        help_texts = {
            'username': _('longitud mínima 6 cáracteres'),
            'first_name': _('No es obligatorio'),
            'last_name': _('No es obligatorio'),
        }
        error_messages = {
            'username': {
                'max_length': _("Longitud no válida"),
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
                    'username':  forms.TextInput(attrs={'class':'form-control',}),
                    'first_name':  forms.TextInput(attrs={'class':'form-control',}),
                    'email':forms.EmailInput(attrs={'class':'form-control',}),

                }
class UserProfileForm(forms.ModelForm):
    """ Clase formulario detalles adicionales sobre el usuario"""


    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)

        labels = {

                'profile_pic': _('Imagen de perfil:'),

                }
        help_texts = {

        }
        widgets = {

        }

class GroupForm(forms.ModelForm):
    """ FORMULARIO PARA CREAR GRUPOS"""


    class Meta():
        model = UserGroup
        fields = ('group_name', 'group_description', 'max_members', 'group_color', )
        labels = {
                'group_name': _('Nombre del grupo'),
                'group_description': _('Describe el grupo'),
                'max_members': _('Número máximo de miembros'),
                'group_color': _('Color del grupo'),
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

    group_code = forms.CharField(label='Código de invitación:', widget=forms.TextInput(attrs={'required': 'required', 'class': 'form-control', }))

    def clean(self):
        all_clean_data = super( JoinGroupForm, self).clean()
        group_code = all_clean_data['group_code']