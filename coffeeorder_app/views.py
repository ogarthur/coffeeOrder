from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.db.models import Q
# 3rd
from datetime import datetime, timedelta

from account_app.forms import JoinGroupForm
from .forms import AddBarForm, AddProductForm, AddProductVariationForm


from .model.orderlist import OrderList
from .model.bar import Bar
from account_app.models import UserGroup

# #########BAR###############################


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

# #########BAR###############################


@login_required
def add_bar(request, group_id):
    registered = False
    if request.method == "POST":
        bar_form = AddBarForm(request.POST)
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


@login_required
def get_bar(request):
    pass


@login_required
def delete_bar(request):
    pass


@login_required
def update_bar(request):
    pass

# #########ENDBAR###############################
# #########ORDER LISTS#########################


@login_required
def menu_order_list(request, group_id):
    group = UserGroup.objects.get(id=group_id)
    official_bar = Bar.objects.filter( bar_official=True)
    return render(request, 'coffeeorder_app/menuOrderList.html', {'group': group, 'official_bar': official_bar})


@login_required
def add_order_list(request, group_id, bar_id):
    bar = Bar.objects.get(id=bar_id)
    group = UserGroup.objects.get(id=group_id)
    orders = OrderList.objects.filter(order_group=group)
    free = True

    for checkorder in orders:
        print("BAR", bar == checkorder.order_bar )
        print("GROUP",group ==checkorder.order_group)
        if bar == checkorder.order_bar and group == checkorder.order_group:
            free = False
            break;
    print("FINAL",free)
    if free:
        order_list = OrderList()
        time_created = datetime.today()
        time_expiration = time_created + timedelta(hours=2)
        order_list.created = time_created
        order_list.expiration = time_expiration
        order_list.order_bar = bar
        order_list.order_group = group
        order_list.save()

    response = '/account_app/group/{}'.format(group_id)
    return redirect(response)


@login_required
def delete_order_list(request, group_id, order_list_id):
    OrderList.objects.get(id=order_list_id).delete()
    response = '/account_app/group/{}'.format(group_id)
    return redirect(response)


def check_order(request):
    today = datetime.today()

    orders = OrderList.objects.filter(Q(expiration__lte=today))

    for o in orders:

        o.delete()
    print("CHECKEANDO SI HAY QUE ELIMINARs")
    return redirect(index)
# ###########END ORDER LIST################
# #############ORDERS#######################


@login_required
def get_order(request, order_id):
    pass


@login_required
def create_order(request, order_list_id):
    pass


@login_required
def update_order(request, order_id):
    pass


@login_required
def delete_order(request, order_id):
    pass


# ############END ORDERS ################
# ############PRODUCTS   ################


@login_required
def get_product(request, product_id):
    pass


@login_required
def get_product_variation(request, product_variation_id):
    pass


@login_required
def add_product(request):

    if request.method == "POST":
        product_form = AddProductForm(request.POST)
        product_variation_form = AddProductVariationForm(request.POST)
        if product_form.is_valid() and product_variation_form.is_valid():
            product = product_form.save()
            if product_variation_form.cleaned_data['product_variation_name'] != "NONE" and product_variation_form.cleaned_data['product_variation_name'] !=" " :

                product_variation = product_variation_form
                product_variation.product_variation_product = product
                product_variation.save()

            return redirect('coffeeorder_app:add_product')

        elif product_form.is_valid():
            product_form.save()
            return redirect('coffeeorder_app:add_product')
        else:
            print(product_form.errors)
    else:
        product_form = AddProductForm()
        product_variation_form = AddProductVariationForm()
    return render(request, 'coffeeorder_app/addProduct.html', {
        'product_form': product_form,
        'product_variation_form': product_variation_form,
    })


@login_required
def add_product_variation(request, product_id):
    pass


@login_required
def assignate_product_to_bar(request, group_id, bar_id, product_id, product_variation_id):
    pass


@login_required
def delete_product(request, product_id):
    pass


@login_required
def delete_product_variation(request, product_variation_id):
    pass


@login_required
def update_product(request, product_id):
    pass


@login_required
def update_product_variation(request, product_variation_id):
    pass

