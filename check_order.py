from coffeeorder_app.model.orderlist import OrderList
from datetime import datetime, timedelta

def check_order(self):

    orders = OrderList.objects.filter(expiration__lte=datetime.today())
    for o in orders:
        print(orders);
if __name__ == '__main__':
    print("ELIMINANDO ORDENES EXPIRADAS")