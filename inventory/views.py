from django.shortcuts import render
from .models import Inventory
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def add_inventory(request):
    if request.method == "POST":
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        Inventory.objects.create(name=name, 
                                 quantity=quantity, 
                                 price=price)
        return HttpResponseRedirect('/view')

    return render(request, 'add_inventory.html')


def view_inventory(request):
    inventories = Inventory.objects.all()
    return render(request, 'view_inventory.html', {'inventories': inventories})

# This is to delete products in our inventory 
def delete_inventory(request, inventory_id):
    inventory = Inventory.objects.get(id=inventory_id)
    inventory.delete()
    return HttpResponseRedirect('/view')

# This is for Edition out inventory 
def update_inventory(request, inventory_id):
    inventory = Inventory.objects.get(id=inventory_id)
    if request.method == "POST":
        inventory.name = request.POST.get('name')
        inventory.quantity = request.POST.get('quantity')
        inventory.price = request.POST.get('price')
        inventory.save()
        return HttpResponseRedirect('/view')

    return render(request, 'update_inventory.html', {'inventory': inventory})