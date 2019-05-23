from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from coffeeorder_app.model.bar import Bar
from coffeeorder_app.model.product import Product, ProductVariation


class AddBarForm(forms.ModelForm):

    class Meta:
        model = Bar
        msg_required = "Obligatory field"

        fields = (
            'bar_name',
            'bar_description',
            'bar_color',
        )

        fields_required = (
            'bar_name',
        )
        labels = {
            'bar_name': _("Bar's Name"),
            'bar_description': _("Description of the bar"),
            'bar_color': _("Bar card color"),
        }
        error_messages = {
            'bar_name': {
                'required': _(msg_required)
            }
        }
        widgets = {
            'bar_name': forms.TextInput(attrs={'class': 'form-control', }),
            'bar_description': forms.TextInput(attrs={'class': 'form-control', }),
            'bar_color': forms.TextInput(attrs={'class': 'form-control  color-menu', }),
        }
