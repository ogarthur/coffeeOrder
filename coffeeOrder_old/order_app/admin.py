from django.contrib import admin

# Register your models here.
from .model.bar import Bar
from .model import combo
from .model.friendGroup import FriendGroup
from .model.orderlist import OrderList
from .model.product import Product, BarProduct, ProductVariation

admin.site.register(Bar)
admin.site.register(combo.Combo)
admin.site.register(FriendGroup)
admin.site.register(OrderList)
admin.site.register([Product, BarProduct, ProductVariation])
