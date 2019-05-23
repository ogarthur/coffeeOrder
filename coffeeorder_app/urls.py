from django.contrib import admin
from django.urls import path, include
from coffeeorder_app.views import bar_views, order_views, product_views, views

app_name = 'coffeeorder_app'

urlpatterns = [
    path('group/<int:group_id>', views.get_group_page,name='get_group_page'),
    path('<int:group_id>/addbar/', bar_views.add_bar, name='add_bar'),
    path('<int:group_id>/menuorderlist/', order_views.menu_order_list, name='menu_order_list'),
    path('<int:group_id>/addorderlist/<int:bar_id>', order_views.add_order_list, name='add_order_list'),
    path('<int:group_id>/deleteorderlist/<int:order_list_id>', order_views.delete_order_list, name='delete_order_list'),
    path('addproduct/', product_views.add_product, name='add_product'),
    path('<int:group_id>/addproductbar/<int:bar_id>', product_views.add_product_bar, name='views.add_product_bar'),
    path('add_order/<int:order_list_id>', order_views.add_order, name='add_order'),
    path('product_to_order/<int:order>/<int:product>/<int:add>', order_views.product_to_order,
         name='product_to_order'),


    path('checkorder', order_views.check_order, name="check_order"),
]
