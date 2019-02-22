from django.contrib import admin

# Register your model here.
from  .model.bar import Bar
from .model.combo import Combo
from .model.group import Group
from .model.orderlist import OrderList
from .model.product import Product, ProductBar

admin.register(Bar)
admin.register(Combo)
admin.register(Group)
admin.register(OrderList)
admin.register([Product, ProductBar])
