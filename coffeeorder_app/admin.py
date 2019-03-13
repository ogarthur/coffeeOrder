from django.contrib import admin
from .model.bar import Bar
from .model.product import Product,ProductVariation
# Register your model here.

admin.site.register(Bar)
admin.site.register([ProductVariation, Product])

