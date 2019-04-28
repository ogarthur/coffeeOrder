from django.shortcuts import render
# 3rd

from account_app.forms import JoinGroupForm

from ..model.order import OrderList
from account_app.models import UserGroup


def index(request):
    """Funcion que devuelve la vista principal de la página"""
    data = {}
    if request.user.is_authenticated:

        groupForm = JoinGroupForm()
        groups = UserGroup.objects.filter(group_members=request.user).values()
        order_list = []
        for g in groups:
            orders= OrderList.objects.filter(order_group_id=g['id'])
            for o in orders:
                order_list.append(o)
        if request.method == 'POST':
            warning = {
                        '0': 'Te has unido al grupo!',
                        '1': 'Grupo no existente',
                        '2': 'Ya perteneces al grupo',
                        '3': 'El grupo esta lleno',
                        '4': 'Error',
            }

            group_form_post = JoinGroupForm(request.POST)
            codigo_obt = request.POST.get('group_code')
            print(codigo_obt)
            if group_form_post.is_valid():
                print("valid")
                if UserGroup.objects.filter(group_code=codigo_obt).exists():
                    group_to_join = UserGroup.objects.get(group_code=codigo_obt)
                    members = group_to_join.group_members.count()
                    print("valid2")
                    if (members+1) <= group_to_join.max_members:
                        if group_to_join.group_members.filter(pk=request.user.pk).exists():
                            return render(request, 'coffeeorder_app/home.html', {'groups': groups, 'join_group_form': groupForm, 'warning': warning['2'],'order_list':order_list})
                        else:
                            group_to_join.group_members.add(request.user)
                            group_to_join.save()
                            return render(request, 'coffeeorder_app/home.html', {'groups': groups, 'join_group_form': groupForm, 'warning': warning['0'],'order_list':order_list})
                    else:
                        return render(request, 'coffeeorder_app/home.html', {'groups': groups, 'join_group_form': groupForm, 'warning': warning['3'],'order_list':order_list})
                else:
                    return render(request, 'coffeeorder_app/home.html', {'groups': groups, 'join_group_form': groupForm, 'warning': warning['1'],'order_list':order_list})
            else:
                print("form no valid")
                return render(request, 'coffeeorder_app/home.html', {'groups': groups, 'join_group_form': groupForm, 'warning': warning['4'],'order_list':order_list})
        else:
            return render(request, 'coffeeorder_app/home.html', {'groups':groups, 'join_group_form': groupForm,'order_list':order_list})
    else:
        return render(request, 'account_app/login.html')








