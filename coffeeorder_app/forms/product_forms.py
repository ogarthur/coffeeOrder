from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from coffeeorder_app.model.bar import Bar
from coffeeorder_app.model.product import Product, ProductVariation,ProductBar


msg_required = "Obligatory field"


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = (
            'product_name',
            'product_color',
            'product_type',
        )

        fields_required = (
            'product_name',
            'product_type',
        )
        labels = {
            'product_name': _('Name'),
            'product_type': _('Type of product'),
            'product_color': _('Color'),
        }
        help_texts = {
            'product_color': _('Choose the color for the card of the product')
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

#class selectProductForm(forms.Form):
 #       product = none


class AddProductBarForm(forms.ModelForm):

    class Meta:
        model = ProductBar


        fields = (
            'product_bar_prize',
            'product_bar_stock',
        )

        fields_required = (
            'product_bar_prize',
        )
        labels = {
            'product_bar_prize': _('Prize'),
            'product_bar_stock': _('Stock'),
        }

        error_messages = {
            'product_bar_prize': {
                'required': _(msg_required)
            }
        }
        widgets = {
            'product_bar_prize': forms.TextInput(attrs={'class': 'form-control', }),
            'product_bar_stock': forms.CheckboxInput(attrs={'class': 'form-control  color-menu', }),
        }