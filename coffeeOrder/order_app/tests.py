from django.test import TestCase

# Create your tests here.

from order_app.model.bar import Bar
from order_app.model.combo import Combo
from order_app.model.friendGroup import FriendGroup
from order_app.model.orderlist import OrderList
from order_app.model.product import Product, BarProduct, ProductVariation
from django.contrib.auth.models import User


class OrderTestCase(TestCase):

    def setUp(self):
        cont = 1
        #TEST USERS
        User.objects.create(username="juan_u", email="juang@gmail.com", password="kartoffel")
        User.objects.create(username="lucas_u", email="lucas@gmail.com", password="kartoffel")
        User.objects.create(username="sara_u", email="sara@gmail.com", password="kartoffel")
        User.objects.create(username="arthur_u", email="arthur@gmail.com", password="kartoffel")
        User.objects.create(username="bart_u", email="bart@gmail.com", password="kartoffel")
        User.objects.create(username="lisa_u", email="lisa@gmail.com", password="kartoffel")
        User.objects.create(username="homer_u", email="homer@gmail.com", password="kartoffel")

        #FRIEND TEST GROUPS
        FriendGroup.objects.create(group_name="grupo1", group_description="primer grupo")
        FriendGroup.objects.create(group_name="grupo2", group_description="segundo grupo")

        for user in User.objects.all():
            if cont % 2 != 0:
                FriendGroup.objects.get(group_name="grupo1").members.add(user)
            else:
                FriendGroup.objects.get(group_name="grupo2").members.add(user)
            cont += 1

        #TEST BARS
        Bar.objects.create(bar_name="kiwi")
        Bar.objects.create(bar_name="provenza")
        Bar.objects.create(bar_name="alborada")

        #TEST PRODUCTS
        Product.objects.create(product_name="black coffee", product_description="")
        Product.objects.create(product_name="juice", product_description="")
        Product.objects.create(product_name="colacao", product_description="")
        Product.objects.create(product_name="te", product_description="")

        te = Product.objects.get(product_name="te")

        #TEST PRODUCT VARIATIONS
        ProductVariation.objects.create(product_variation_name="verde", product=te, )

        #TEST PRODUCT IN BAR
        BarProduct.objects.create(bar_product_prize="3.00",bar_product_stock=True)

        #TEST COMBOS



        #TEST ORDER LIST

    def test_get_bar(self):


        bar = Bar.objects.get(name="kiwi")
        self.assertEqual(bar.bar_logo, 'default.png')

