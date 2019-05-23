from django.contrib import admin
from .model.bar import Bar
from .model.product import Product, ProductVariation, ProductBar
from .model.order import OrderList, Order, OrderItem
# Register your model here.

admin.site.register(Bar)
admin.site.register([OrderList, Order, OrderItem])
admin.site.register([Product, ProductBar])

