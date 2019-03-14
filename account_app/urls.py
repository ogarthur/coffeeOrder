from django.contrib import admin
from django.urls import path, include
from account_app import views
from django.conf import settings
from django.conf.urls.static import static
#template tag
app_name = 'account_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('user/<int:user_id>/', views.get_profile, name='get_profile'),
    path('create_group/', views.create_group, name="create_group"),
    path('delete_group/<int:group_id>/', views.delete_group, name="delete_group"),
    path('delete_from_group/<int:group_id>/<int:user_id>', views.delete_user_from_group, name="delete_from_group"),
    path('group/<int:group_id>', views.get_group_page, name='get_group_page'),
    path('abandon_group/<int:group_id>', views.abandon_group, name="abandon_group"),
    path('close_group/<int:group_id>', views.close_group, name="close_group"),


]
