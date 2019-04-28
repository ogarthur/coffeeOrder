from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# 3rd

from coffeeorder_app.forms.product_forms import AddProductForm

from ..model.product import Product


@login_required
def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    pass


@login_required
def get_product_variation(request, product_variation_id):
    pass


@login_required
def add_product(request):

    if request.method == "POST":
        product_form = AddProductForm(request.POST)

        if product_form.is_valid():
            product_form.save()
            return redirect('coffeeorder_app:add_product')
        else:
            print(product_form.errors)
    else:
        product_form = AddProductForm()

    return render(request, 'coffeeorder_app/addProduct.html', {
        'product_form': product_form,

    })


@login_required
def add_product_bar(request,bar_id, product_id):
    return render(request, 'coffeeorder_app/addProductBar.html',)



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
