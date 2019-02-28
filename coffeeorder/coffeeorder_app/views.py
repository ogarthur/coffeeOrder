from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from account_app.forms import JoinGroupForm
from account_app.models import  UserGroup
# Create your views here.

def index(request):
    """Funcion que devuelve la vista principal de la página"""
    data = {}
    if request.user.is_authenticated:
        groupForm = JoinGroupForm()
        groups = UserGroup.objects.filter(group_members=request.user).values()
        if request.method == 'POST':
            warning={'0':'Te has unido al grupo!',
                     '1':'Grupo no existente',
                     '2':'Ya perteneces al grupo',
                     '3':'El grupo esta lleno',
                     '4':'Error',
                     }
            groupFormPost = JoinGroupForm(request.POST)
            codigo_obt = request.POST.get('group_code')
            print(codigo_obt)
            if groupFormPost.is_valid():
                print("valid")
                if UserGroup.objects.filter(group_code=codigo_obt).exists():
                    group_to_join = UserGroup.objects.get(group_code=codigo_obt)
                    members = group_to_join.group_members.count()
                    print("valid2")
                    if (members+1)<=group_to_join.max_members :
                        if group_to_join.group_members.filter(pk=request.user.pk).exists():
                            return render(request, 'coffeeorder_app/home.html', {'groups': groups, 'join_group_form': groupForm, 'warning': warning['2']})
                        else:
                            group_to_join.group_members.add(request.user)

                            group_to_join.save()
                            return render(request, 'coffeeorder_app/home.html', {'groups': groups, 'join_group_form': groupForm, 'warning': warning['0']})
                    else:
                        return render(request, 'coffeeorder_app/home.html', {'groups': groups, 'join_group_form': groupForm, 'warning': warning['3']})
                else:
                    return render(request, 'coffeeorder_app/home.html', {'groups': groups, 'join_group_form': groupForm, 'warning': warning['1']})

            else:
                print("form no valid")
                return render(request, 'coffeeorder_app/home.html', {'groups': groups, 'join_group_form': groupForm, 'warning': warning['4']})
        else:
            return render(request, 'coffeeorder_app/home.html', {'groups':groups, 'join_group_form': groupForm, })

    else:
        print("NO LOGEADO")

        return render(request, 'account_app/login.html')

@login_required
def getGroupPage(request, group_id):
    group = UserGroup.objects.get(id=group_id)

    if group.group_members.filter(pk=request.user.pk).exists():
        return render(request, 'coffeeorder_app/groupView.html', {'group': group})
    else:
        return render(request, 'coffeeorder_app/groupView.html', )