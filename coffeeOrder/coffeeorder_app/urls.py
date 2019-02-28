from django.contrib import admin
from django.urls import path,include
from coffeeorder_app import views
#template tag
app_name = 'coffeeorder_app'

urlpatterns = [
    path('group/<int:group_id>', views.getGroupPage, name='get_group_page'),
]
