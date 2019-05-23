from django import forms
from django.core import validators
from django.utils.translation import gettext as _
from coffeeorder_app.model.bar import Bar
from coffeeorder_app.model.product import Product, ProductBar
from coffeeorder_app.model.order import Order,OrderList
msg_required = "Obligatory field"


class SingleOrder(forms.Form):

    class Meta:
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
