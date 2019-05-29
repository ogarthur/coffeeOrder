from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


from datetime import datetime, timedelta
from django.http import JsonResponse
from ..model.order import OrderList, Order, OrderItem
from ..model.bar import Bar
from ..model.product import ProductBar, Product
from account_app.models import UserGroup
from django.db.models import Q


@login_required
def menu_order_list(request, group_id):
    group = UserGroup.objects.get(id=group_id)
    official_bar = Bar.objects.filter(bar_official=True)
    group_bars = Bar.objects.filter(group=group)
    return render(request, 'coffeeorder_app/menuOrderList.html', {'group': group,
                                                                  'official_bar': official_bar,
                                                                  'group_bars': group_bars})


@login_required
def add_order_list(request, group_id, bar_id):
    bar = Bar.objects.get(id=bar_id)
    group = UserGroup.objects.get(id=group_id)
    orders = OrderList.objects.filter(order_group=group, state=True)

    free = True

    for order in orders:
        print(orders)
        if bar == order.order_bar and group == order.order_group:
            free = False
            break
    #free = True
    if free:
        order_list = OrderList()
        time_created = datetime.today()
        time_expiration = time_created + timedelta(hours=2)
        order_list.created = time_created
        order_list.user_creator = request.user
        order_list.expiration = time_expiration
        order_list.order_bar = bar
        order_list.order_group = group
        order_list.save()

    response = '/coffeeorder_app/group/{}'.format(group_id)
    return redirect(response)


@login_required
def delete_order_list(request, group_id, order_list_id):
    order_list = OrderList.objects.get(id=order_list_id)
    order_list.state = False
    order_list.save()
    return redirect('coffeeorder_app:group', group_id=group_id)


@login_required
def modify_order_list(request, order_list_id):
    order = Order.objects.get(id=order_list_id)
    pass


@login_required
def check_order(request):
    today = datetime.today()
    orders = OrderList.objects.filter(Q(expiration__lte=today))

    for order in orders:

        order.state = False
        order.save()

    return redirect('index')


@login_required
def order_ticket(request, order_list_id, individual=False):
    order_list = OrderList.objects.get(pk=order_list_id)
    order_details = {}
    order_prize = 0
    if individual:
        try:
            order = Order.objects.get(order_order_list_id=order_list.id, order_user=request.user)
            products = OrderItem.objects.filter(order=order)
            for prod in products.all():
                try:
                    prize = prod.order_product_bar.product_bar_prize * int(prod.quantity)
                    order_details[prod.order_product_bar.product.product_name] = {
                        'quantity': prod.quantity,
                        'prize': prize,
                        'product_id': prod.order_product_bar.id,
                    }
                    order_prize += prize
                except OrderItem.DoesNotExist:
                    order_details[prod.order_product_bar.product.product_name] = {
                        'quantity': 0,
                        'prize': 0,
                        'product_id': prod.order_product_bar.id,
                    }
        except Order.DoesNotExist:
            pass
    else:
        orders = Order.objects.filter(order_order_list_id=order_list.id)
        for single in orders:
            order_details[single.order_user.username] = {}

            products = OrderItem.objects.filter(order=single)
            for prod in products.all():
                try:
                    prize = prod.order_product_bar.product_bar_prize * int(prod.quantity)
                    order_details[single.order_user.username][prod.order_product_bar.product.product_name] = {
                        'quantity': prod.quantity,
                        'prize': prize,
                        'product_id': prod.order_product_bar.id,
                    }
                    order_prize += prize
                except OrderItem.DoesNotExist:
                    order_details[single.order_user.username][prod.order_product_bar.product.product_name] = {
                    'quantity': 0,
                    'prize': 0,
                    'product_id': prod.order_product_bar.id,
                }

    return order_details, order_prize

@login_required
def product_to_order(request, order, product, add=2):

    try:
        item = OrderItem.objects.get(order_product_bar_id=product,
                                     order_id=order)
    except OrderItem.DoesNotExist:

        order_target = Order.objects.get(pk=order)
        order_product = ProductBar.objects.get(pk=product)
        item = OrderItem.objects.create(order=order_target,
                                        order_product_bar=order_product,
                                        quantity=0)
        item.save()

    if add == 0 and item.quantity > 0:
        item.quantity -= 1
    elif add == 1:
        item.quantity += 1

    if item.quantity == 0 or add == 2:
        item.delete()
    else:
        item.save()

    list_id = Order.objects.get(pk=order).order_order_list.pk
    order_details, order_prize = order_ticket(request, list_id, True)

    data = {
        'order_details': order_details,
        'prize': order_prize
    }
    return JsonResponse(data)


def add_order(request, order_list_id):
    order_list = OrderList.objects.get(pk=order_list_id)

    bar = Bar.objects.get(bar_name=order_list.order_bar.bar_name)
    products_bar = ProductBar.objects.filter(product_bar_bar=bar.id)
    food_list, drink_list = [], []
    try:
        order = Order.objects.get(order_order_list_id=order_list.id,
                                  order_user=request.user)

    except Order.DoesNotExist:
        '''no order found'''
    except Order.MultipleObjectsReturned:
        '''multiples orders'''

    order_details, order_prize = order_ticket(request, order_list_id, True)
    for product in products_bar:
        product_ins = Product.objects.get(id=product.product.id)
        if product_ins.product_type is '0':
            food_list.append({'product_id': product.id,
                              'name': product_ins.product_name,
                              'prize': product.product_bar_prize,
                              'color': product_ins.product_color})
        else:
            drink_list.append({
                'product_id': product.id,
                'name': product_ins.product_name,
                'prize': product.product_bar_prize,
                'color': product_ins.product_color})
    return render(request, 'coffeeorder_app/addOrder.html',
                  {'food_list': food_list,
                   'drink_list': drink_list,
                   'order_details': order_details,
                   'order_prize': order_prize,
                   'order_id': order.id}
                  )


def update_order(request):
    order_updated = {}
    return order_updated


@login_required
def get_order(request, order_id):
    order = Order.objects.get(id=order_id)
    pass


@login_required
def modify_order(request, order_id):
    order = Order.objects.get(id=order_id)
    pass


@login_required
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    pass
