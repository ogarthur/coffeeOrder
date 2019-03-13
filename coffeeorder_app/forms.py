from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from .model.bar import Bar
from .model.product import Product, ProductVariation


class AddBarForm(forms.ModelForm):

    class Meta:
        model = Bar
        msg_required = "Campo obligatorio"

        fields = (
            'bar_name',
            'bar_description',
            'bar_color',
        )

        fields_required = (
            'bar_name',
        )
        labels = {
            'bar_name': _('Nombre del bar'),
            'bar_description': _("Datos del bar"),
            'bar_color': _("Color del bar"),
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


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        msg_required = "Campo obligatorio"

        fields = (
            'product_name',
            'product_color',
        )

        fields_required = (
            'product_name',
        )
        labels = {
            'product_name': _('Nombre'),
            'product_color': _('color'),
        }
        error_messages = {
            'product_name': {
                'required': _(msg_required)
            }
        }
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', }),
            'product_color': forms.TextInput(attrs={'class': 'form-control  color-menu', }),
        }


class AddProductVariationForm(forms.ModelForm):

    class Meta:
        model = ProductVariation

        msg_required = "Campo obligatorio"

        fields = (
            'product_variation_name',
        )
        fields_required = (

        )

        labels = {
            'product_variation_name': _('Variación del producto(TIPO)'),
        }
        error_messages = {
            'product_variation_name': {
                'required': _(msg_required)
            }
        }
        widgets = {
            'product_variation_name': forms.TextInput(attrs={'class': 'form-control', }),
        }
