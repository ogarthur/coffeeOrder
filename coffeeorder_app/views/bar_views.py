from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from coffeeorder_app.forms.bar_forms import AddBarForm

from ..model.bar import Bar
from account_app.models import UserGroup



@login_required
def add_bar(request, group_id):
    registered = False
    if request.method == "POST":
        bar_form = AddBarForm(request.POST)
        if bar_form.is_valid():
            group = UserGroup.objects.get(id=group_id)
            bar = bar_form.save()
            bar.group.add(group)
            bar_form.save()
            registered = True
            return redirect('index')
        else:
            print(bar_form.errors)
    else:
        bar_form = AddBarForm()
    return render(request, 'coffeeorder_app/addBar.html', {'bar_form': bar_form, 'registered': registered})


@login_required
def get_bar(request, bar_id):
    bar = Bar.objects.get(id=bar_id)
    return bar


@login_required
def delete_bar(request, bar_id):
    if Bar.objects.get(id=bar_id).delete():
        Bar.objects.get(id=bar_id).delete()
        return True
    else:
        return False


@login_required
def modify_bar(request, bar_id):
    bar = Bar.objects.get(id=bar_id)
    pass

