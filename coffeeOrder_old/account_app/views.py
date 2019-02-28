from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from account_app.forms import UserForm, UserProfileForm

# Create your views here.
##########################################REGISTRO/LOGIN##################################################
#REGISTRO

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,'account_app/registration.html',
    {'user_form':user_form,
    'registered':registered})

#LOGIN
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Cuenta no activa")
        else:
            print("Someone tried to login and failed")
            print("Username: {}  with password :{}".format(username,password))
            return render(request,'account_app/login.html', {'login_error':'Credeenciales no válidos'})
    else:
        return render(request,'account_app/login.html', {})


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
    u.delete()
    logout(request)
    return HttpResponseRedirect(reverse('index'))
