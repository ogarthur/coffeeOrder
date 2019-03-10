from django.shortcuts import render
from . import forms
from django.utils.translation import gettext as _
#
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt


from .forms import UserForm, UserProfileForm, GroupForm
from .models import UserProfileInfo, UserGroup
from django.contrib.auth.models import User
import random, string

app_name = 'account_app'
# Create your views here.




##########################################REGISTRO/LOGIN##################################################
#REGISTRO

def is_admin(group_id,user_id):
    group = UserGroup.objects.get(id=group_id)

    if group.group_admin.filter(pk=user_id).exists():
        return True
    else:
        return False

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

            return redirect('index')
        else:
            print(user_form.errors,profile_form.errors)
            return render(request, '{}/registration.html'.format(app_name),
                          {'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

        return render(request,'{}/registration.html'.format(app_name),
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

                    request.session['profile_pic'] = user_info[0]
                return redirect('index')

            else:
                return HttpResponse("Cuenta no activa")
        else:
            print("Someone tried to login and failed")
            print("Username: {}  with password :{}".format(username,password))
            return render(request, '{}/login.html'.format(app_name), {'login_error':'Credeenciales no válidos'})
    else:
        return render(request, '{}/login.html'.format(app_name),{})


#LOGOUT
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def delete_user(request):
    from django.contrib.auth.models import User
    print("borrando")
    user = User.objects.get(username=request.user.username)
    groups = UserGroup.objects.filter(group_admin=user)
    for group in groups:
        print(group.group_members)
        if group.group_members.count() == 1:
            delete_group(group.id)
    user.delete()
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def delete_group(request, group_id):

    print("borrando")
    group_to_delete = UserGroup.objects.get(id=group_id)
    print("here")
    if is_admin(group_id,request.user.id):

        group_to_delete.delete()

    return redirect('index')

@login_required
def delete_user_from_group(request, group_id, user_id):
    from django.contrib.auth.models import User
    group = UserGroup.objects.get(id=group_id)
    user_to_delete = User.objects.get(id=user_id)
    if group.group_admin.filter(pk=request.user.pk).exists():
        group.group_admin.remove(user_to_delete)
        group.group_members.remove(user_to_delete)
    response = '/account_app/group/{}'.format(group.id)
    return redirect(response )


@login_required
def abandon_group(request, group_id):
    group_to_delete = UserGroup.objects.get(id=group_id)

    group_to_delete.group_members.remove(request.user)
    if group_to_delete.group_members.count() == 0:
        delete_group(group_id)
    return redirect('index')


@login_required
def get_profile(request, user_id):
    user = User.objects.get(id=user_id)
    pic = UserProfileInfo.objects.get(user=user)
    groups_in = UserGroup.objects.filter(group_members=user).values()
    user_data = {
        'user': user,
        'profile_pic': pic.profile_pic,
        'groups_in':groups_in,
    }
    print(user_data)

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
            if not group.group_pic:
                group.group_pic = 'group_pics/group.png'
            group.save()
            registered = True
            return redirect('index')
        else:
            print(group_form.errors)
    else:
        group_form = GroupForm()
        print("CREADO FORMULARIO")
    return render(request, '{}/creategroup.html'.format(app_name), {'group_form': group_form, 'registered': registered})

@login_required
def getGroupPage(request, group_id):
    group = UserGroup.objects.get(id=group_id)

    members = {}


    for g in group.group_members.all():

        user = User.objects.get(id=g.id)

        pic = UserProfileInfo.objects.get(user=user)

        members[g.id]= {

            'username' : g.username,
            'name' : g.first_name,
            'profile_pic' : pic.profile_pic,
        }
    print(members)
    if group.group_members.filter(pk=request.user.pk).exists():

        if is_admin(group_id, request.user.id):
            admin = True
        else:
            print('NO ES ADMIN...')
            admin = False


        return render(request, '{}/groupView.html'.format(app_name), {'group': group,'members':members, 'admin': admin})
    else:
        return render(request, '{}/groupView.html'.format(app_name), )
