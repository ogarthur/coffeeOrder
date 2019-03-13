from django.contrib import admin
from django.urls import path,include
from coffeeorder_app import views
#template tag
app_name = 'coffeeorder_app'

urlpatterns = [
    path('<int:group_id>/addbar/', views.add_bar, name='add_bar'),
    path('<int:group_id>/menuorderlist/', views.menu_order_list, name='menu_order_list'),
    path('<int:group_id>/addorderlist/', views.add_order_list, name='add_order_list'),
    path('addproduct/', views.add_product, name='add_product'),
]
