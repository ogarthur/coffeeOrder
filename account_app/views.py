from django.shortcuts import render
from . import forms
from django.utils.translation import gettext as _
#
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from .forms import CustomUserCreationForm, GroupForm
from .models import CustomUser, UserGroup
from coffeeorder_app.model.order import OrderList
from django.contrib.auth.models import User
import random, string
from .decorators import is_group_admin
app_name = 'account_app'
# Create your views here.




# #################USER##################

def is_admin(group_id,user_id):
    group = UserGroup.objects.get(id=group_id)

    if group.group_admin.filter(pk=user_id).exists():
        return True
    else:
        return False

def register(request):
    registered = False
    if request.method == "POST":
        #user_form = UserForm(data=request.POST)
        user_form = CustomUserCreationForm(request.POST, request.FILES)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

            return redirect('index')
        else:
            print(user_form.errors)
            return render(request, '{}/registration.html'.format(app_name),
                          {'user_form': user_form,
                           'registered': registered})
    else:
        user_form = CustomUserCreationForm()
        return render(request,'{}/registration.html'.format(app_name),
        {'user_form': user_form,
        'registered': registered})


#LOGIN
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')

            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} ".format(username))
            return render(request, '{}/login.html'.format(app_name), {'login_error':'Credeenciales no válidos'})
    else:
        return render(request, '{}/login.html'.format(app_name), {})


# LOGOUT
@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


@login_required
def delete_user(request):
    from django.contrib.auth.models import User

    user = CustomUser.objects.get(username=request.user.username)
    groups = UserGroup.objects.filter(group_admin=user)
    for group in groups:

        if group.group_members.count() == 1:
            delete_group(group.id)
    user.delete()
    logout(request)
    return redirect('index')


@login_required
def delete_user_from_group(request, group_id, user_id):
    from django.contrib.auth.models import User
    group = UserGroup.objects.get(id=group_id)
    user_to_delete = CustomUser.objects.get(id=user_id)
    if group.group_admin.filter(pk=request.user.pk).exists():
        group.group_admin.remove(user_to_delete)
        group.group_members.remove(user_to_delete)
    response = '/account_app/group/{}'.format(group.id)
    return redirect(response)


# ###########ENDUSER###########################
# ##########group###############

@login_required
def delete_group(request, group_id):

    group_to_delete = UserGroup.objects.get(id=group_id)
    if is_admin(group_id, request.user.id):
        group_to_delete.delete()

    return redirect('index')


@login_required
def abandon_group(request, group_id):
    print("xxxABANDONING")
    group_to_abandon = UserGroup.objects.get(id=group_id)
    group_to_abandon.group_members.remove(request.user)
    print("ABANDONING")
    if group_to_abandon.group_members.count() == 0:
        print("GRUPO VACIO")
        delete_group(request, group_id)

    return redirect('index')


@login_required
def get_profile(request, user_id):
    user = CustomUser.objects.get(id=user_id)

    groups_in = UserGroup.objects.filter(group_members=user).values()
    user_data = {
        'user': user,
        'groups_in': groups_in,
    }

    return render(request, '{}/userProfile.html'.format(app_name), {'user_data': user_data})


@login_required
def create_group(request):
    registered = False
    if request.method == "POST":
        group_form = GroupForm(request.POST, request.FILES)
        if group_form.is_valid():
            group = group_form.save()
            group.group_code = ''.join(random.choices(string.ascii_letters + string.digits, k=4)).upper()
            group.group_admin.add(request.user)
            group.group_members.add(request.user)
            group.save()
            registered = True
            return redirect('index')
        else:
            print(group_form.errors)
    else:
        group_form = GroupForm()
    return render(request, '{}/creategroup.html'.format(app_name), {'group_form': group_form, 'registered': registered})


@login_required
def get_group_page(request, group_id):
    group = UserGroup.objects.get(id=group_id)
    members = {}

    for g in group.group_members.all():

        user = CustomUser.objects.get(id=g.id)
        members[g.id] = {
            'username': g.username,
            'name': g.first_name,
            'profile_pic': g.profile_pic,
        }
        order_list = OrderList.objects.filter(order_group=group)

    if group.group_members.filter(pk=request.user.pk).exists():

        if is_admin(group_id, request.user.id):
            admin = True
        else:
            print('NO ES ADMIN...')
            admin = False
        return render(request, 'coffeeorder_app/groupPage.html',{
            'group': group,
            'members': members,
            'admin': admin,
            'order_list': order_list,

        })
    else:
        return render(request, 'coffeeorder_app/groupPage.html' )


@login_required
def close_group(request, group_id):
    group = UserGroup.objects.get(id=group_id)
    if is_admin(group_id, request.user.id):
        if group.closed:
            print("IS OPEN")
            group.closed = False
            group.save()
        else:
            print("IS NO OPEN")
            group.closed = True
            print(group.closed)
            group.save()
    data = {
        'is_closed': group.closed
    }
    return JsonResponse(data)
# ##########END GROUP###################