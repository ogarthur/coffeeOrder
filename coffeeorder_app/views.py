from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import redirect

from account_app.forms import JoinGroupForm
from .forms import AddBarForm

from account_app.models import UserGroup

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


# #########BAR###############################

def add_bar(request, group_id):
    registered = False
    if request.method == "POST":

        bar_form = AddBarForm(request.POST, request.FILES)

        if bar_form.is_valid():
            group = UserGroup.objects.get(id=group_id)
            bar = bar_form.save()
            group.group_bar.add(bar)
            group.save()
            registered = True
            return redirect('index')
        else:
            print(bar_form.errors)
    else:
        bar_form = AddBarForm()

    return render(request, 'coffeeorder_app/addBar.html', {'bar_form': bar_form, 'registered': registered})


def get_bar(request):
    pass


def delete_bar(request):
    pass


def update_bar(request):
    pass

# #########ENDBAR###############################
# #########ORDER LISTS#########################


def menu_order_list(request, group_id):
    group = UserGroup.objects.get(id=group_id)

    return render(request, 'coffeeorder_app/menuOrderList.html',{'group':group,})


def add_order_list(request,group_id,bar_id):
    pass


def delete_order_list(request,order_list_id):
    pass

# ###########END ORDER LIST################

# #############ORDERS#######################


def get_order(request,order_id):
    pass


def create_order(request,order_list_id):
    pass


def update_order(request,order_id):
    pass


def delete_order(request,order_id):
    pass



# ############END ORDERS ################


def get_product(request,product_id):
    pass


def get_product_variation(request,product_variation_id):
    pass


def create_product(request,bar_id=None):
    pass


def create_product_variation(request,product_id):
    pass


def delete_product(request,product_id):
    pass


def delete_product_variation(request,product_variation_id):
    pass


def update_product(request,product_id):
    pass


def update_product_variation(request,product_variation_id):
    pass