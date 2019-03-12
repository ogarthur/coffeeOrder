from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from .model.bar import Bar
from django.core.files.images import get_image_dimensions


class AddBarForm(forms.ModelForm):

    class Meta:
        model = Bar
        msg_required = "Campo obligatorio"

        fields = (
            'bar_name',
            'bar_info',
            'bar_color',
        )

        fields_required = (
            'bar_name',
        )
        labels = {
            'bar_name': _('Nombre del bar'),
            'bar_info': _("Datos del bar"),
            'bar_color': _("Color del bar"),
        }
        error_messages = {
            'bar_name': {

                'required': _(msg_required)
            }
        }
        widgets = {
            'bar_name': forms.TextInput(attrs={'class': 'form-control', }),
            'bar_info': forms.TextInput(attrs={'class': 'form-control', }),
            'bar_color': forms.TextInput(attrs={'class': 'form-control  color-menu', }),
        }

