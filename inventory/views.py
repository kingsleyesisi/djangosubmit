from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all()
    data = {
        'products': products
        }
    return render(request, 'products.html', data)

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        product = Product(name=name, price=price, quantity=quantity)
        product.save()
        return HttpResponse("Product added successfully!<br><a href='/products/'>Go to product list</a>")
    return render(request, 'add_product.html')

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.save()
        return HttpResponse("Product updated successfully! <br><a href='/products/'>Go to product list</a>")
    return render(request, 'edit_product.html', {'product': product})


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return HttpResponse("Product deleted successfully!")
    return render(request, 'delete_product.html', {'product': product})