from django.shortcuts import render
# 3rd
import json
from account_app.forms import JoinGroupForm

from ..model.order import OrderList, Order
from account_app.models import UserGroup
from django.contrib.auth.decorators import login_required
from account_app.models import CustomUser, UserGroup
from account_app.views import is_admin
from .order_views import order_ticket


def index(request):
    """  MAIN PAGE """
    data = {}
    if request.user.is_authenticated:

        group_form = JoinGroupForm()
        groups = UserGroup.objects.filter(group_members=request.user).values()
        order_json = {'all': []}
        for g in groups:
            order_list = OrderList.objects.filter(order_group_id=g['id'])
            order_json['all'].append(order_list)
            for o_l in order_list:
                orders = Order.objects.filter(order_order_list=o_l)
                group_order = [o_l]
                for single_order in orders:
                    group_order.append(single_order)
                #all_order_list.append(group_order)
        all_order_list = []
        if request.method == 'POST':
            warning = {
                        '0': 'You joined the group!',
                        '1': 'Group does not exist',
                        '2': 'You are already a member of this group',
                        '3': 'Group is full or closed, talk with the admin',
                        '4': 'Error',
            }

            group_form_post = JoinGroupForm(request.POST)
            code_obt = request.POST.get('group_code')
            #print(code_obt)
            if group_form_post.is_valid():
                if UserGroup.objects.filter(group_code=code_obt).exists():
                    group_to_join = UserGroup.objects.get(group_code=code_obt)
                    members = group_to_join.group_members.count()
                    if (members+1) <= group_to_join.max_members:
                        if group_to_join.group_members.filter(pk=request.user.pk).exists():
                            return render(request, 'coffeeorder_app/home.html', {'groups': groups,
                                                                                 'join_group_form': group_form,
                                                                                 'warning': warning['2'],
                                                                                 'order_list': all_order_list})
                        else:
                            group_to_join.group_members.add(request.user)
                            group_to_join.save()
                            return render(request, 'coffeeorder_app/home.html', {'groups': groups,
                                                                                 'join_group_form': group_form,
                                                                                 'warning': warning['0'],
                                                                                 'order_list': all_order_list})
                    else:
                        return render(request, 'coffeeorder_app/home.html', {'groups': groups,
                                                                             'join_group_form': group_form,
                                                                             'warning': warning['3'],
                                                                             'order_list': all_order_list})
                else:
                    return render(request, 'coffeeorder_app/home.html', {'groups': groups,
                                                                         'join_group_form': group_form,
                                                                         'warning': warning['1'],
                                                                         'order_list': all_order_list})
            else:
                return render(request, 'coffeeorder_app/home.html', {'groups': groups,
                                                                     'join_group_form': group_form,
                                                                     'warning': warning['4'],
                                                                     'order_list': all_order_list})
        else:
            return render(request, 'coffeeorder_app/home.html', {'groups': groups,
                                                                 'join_group_form': group_form,
                                                                 'order_list': all_order_list})
    else:
        return render(request, 'account_app/login.html')


@login_required
def get_group_page(request, group_id):
    group = UserGroup.objects.get(id=group_id)
    members = {}
    order_list_details = {}
    for g in group.group_members.all():

        members[g.id] = {
            'username': g.username,
            'name': g.first_name,
            'profile_pic': g.profile_pic,
        }
    order_list = OrderList.objects.filter(order_group=group, state=True)
    for order in order_list:
        order_list_details[order.pk] = {}
        order_list_details[order.pk]['order'] = order
        order_list_details[order.pk]['details'], order_list_details[order.id]['prize'] = order_ticket(request, order.pk, False)
        print(order_list_details[order.pk]['order'].created)

    if group.group_members.filter(pk=request.user.pk).exists():

        if is_admin(group_id, request.user.id):
            admin = True
        else:
            admin = False
        return render(request, 'coffeeorder_app/groupPage.html',{
            'group': group,
            'members': members,
            'admin': admin,
            'order_list_details': order_list_details,

        })
    else:
        return render(request, 'coffeeorder_app/groupPage.html')

