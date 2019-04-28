from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q
# 3rd
from datetime import datetime, timedelta
from .views import index

from ..model.order import OrderList, Order
from ..model.bar import Bar
from account_app.models import UserGroup


@login_required
def menu_order_list(request, group_id):
    group = UserGroup.objects.get(id=group_id)
    official_bar = Bar.objects.filter( bar_official=True)
    group_bars = Bar.objects.filter( group=group )
    return render(request, 'coffeeorder_app/menuOrderList.html', {'group': group, 'official_bar': official_bar, 'group_bars': group_bars})


@login_required
def add_order_list(request, group_id, bar_id):
    bar = Bar.objects.get(id=bar_id)
    group = UserGroup.objects.get(id=group_id)
    orders = OrderList.objects.filter(order_group=group)
    free = True

    for checkorder in orders:
        print("BAR", bar == checkorder.order_bar)
        print("GROUP", group == checkorder.order_group)
        if bar == checkorder.order_bar and group == checkorder.order_group:
            free = False
            break
    print("FINAL", free)
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
def delete_order_list(request, order_list_id):
    OrderList.objects.get(id=order_list_id).delete()

    return redirect('index')


@login_required
def modify_order_list(request, order_list_id):
    order = Order.objects.get(id=order_list_id)
    pass


@login_required
def check_order(request):
    today = datetime.today()

    orders = OrderList.objects.filter(Q(expiration__lte=today))

    for order in orders:
        order.delete()
    return redirect(index)

def add_order(request, order_list_id):
    return render(request, 'coffeeorder_app/addOrder.html')


@login_required
def get_order(request, order_id):
    order = Order.objects.get(id=order_id)
    pass


@login_required


@login_required
def modify_order(request, order_id):
    order = Order.objects.get(id=order_id)
    pass


@login_required
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    pass
