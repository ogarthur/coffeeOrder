from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from coffeeorder_app.model.bar import Bar
from coffeeorder_app.model.product import Product, ProductVariation







'''
class AddProductBarForm(forms.ModelForm):

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
'''