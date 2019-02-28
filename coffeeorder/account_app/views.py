from django.shortcuts import render
from . import forms
from django.utils.translation import gettext as _
#
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .forms import UserForm, UserProfileForm, GroupForm
from .models import UserProfileInfo, UserGroup

import random, string

# Create your views here.
##########################################REGISTRO/LOGIN##################################################
#REGISTRO

def register(request):
    registered = False
    if request.method == "POST":
        user_form       = UserForm(data=request.POST)
        profile_form    = UserProfileForm(request.POST,request.FILES)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if(profile.profile_pic=='pic_folder/None/no-img.jpg'):
                profile.profile_pic='profile_pics/avatar.png'
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'account_app/registration.html',
    {'user_form': user_form,
    'profile_form': profile_form,
    'registered': registered})

#LOGIN
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                if UserProfileInfo.objects.filter(user=user).exists():
                    user_info = UserProfileInfo.objects.filter(user=user).values_list('profile_pic', flat=True)
                    print(user_info)
                    request.session['profile_pic'] = user_info[0]
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Cuenta no activa")
        else:
            print("Someone tried to login and failed")
            print("Username: {}  with password :{}".format(username,password))
            return render(request,'account_app/login.html',{'login_error':'Credeenciales no válidos'})
    else:
        return render(request,'account_app/login.html',{})


#LOGOUT
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def delete_user(request):
    from django.contrib.auth.models import User
    print("borrando")
    u = User.objects.get(username=request.user.username)
    print("here")
    u.delete()
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def create_group(request):
    registered = False
    if request.method == "POST":

        group_form = GroupForm(request.POST, request.FILES)

        if group_form.is_valid():

            group = group_form.save()
            #group = UserGroup.objects.get(group_name=group.group_name)
            group.group_code = ''.join(random.choices(string.ascii_letters + string.digits, k=4)).upper()
            group.group_admin.add(request.user)
            group.group_members.add(request.user)
            if not group.group_pic:
                group.group_pic = 'group_pics/group.png'
            group.save()
            registered = True
            print('good!')
        else:
            print(group_form.errors)
    else:
        group_form = GroupForm()
        print("CREADO FORMULARIO")
    return render(request,'account_app/creategroup.html', {'group_form': group_form, 'registered': registered})

def index(request):
    """Funcion que devuelve la vista principal de la página"""
    return render(request,'base.html')