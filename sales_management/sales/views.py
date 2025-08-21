from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Customer, Sale
from .form import ProductForm, CustomerForm, SaleForm

# Home View: Dashboard showing summaries
class HomeView(View):
    def get(self, request):
        total_products = Product.objects.count()
        total_customers = Customer.objects.count()
        total_sales = Sale.objects.count()
        context = {
            'total_products': total_products,
            'total_customers': total_customers,
            'total_sales': total_sales,
        }
        return render(request, 'index.html', context)

# Product Views
class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()  # Get all products
        return render(request, 'product_list.html', {'products': products})

class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product_form.html', {'form': form})
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new product
            return redirect('product_list')  # Redirect to list
        return render(request, 'product_form.html', {'form': form})

class ProductUpdateView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'product_form.html', {'form': form})
    
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'product_form.html', {'form': form})

class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product_confirm_delete.html', {'product': product})
    
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('product_list')

# Similar views for Customer (copy-paste and replace 'Product' with 'Customer')
class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'customer_list.html', {'customers': customers})

class CustomerCreateView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'customer_form.html', {'form': form})
    
    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'customer_form.html', {'form': form})

class CustomerUpdateView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(instance=customer)
        return render(request, 'customer_form.html', {'form': form})
    
    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'customer_form.html', {'form': form})

class CustomerDeleteView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, 'customer_confirm_delete.html', {'customer': customer})
    
    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return redirect('customer_list')

# Similar views for Sale
class SaleListView(View):
    def get(self, request):
        sales = Sale.objects.all()
        return render(request, 'sale_list.html', {'sales': sales})

class SaleCreateView(View):
    def get(self, request):
        form = SaleForm()
        return render(request, 'sale_form.html', {'form': form})
    
    def post(self, request):
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()  # This triggers the save() logic in model
            return redirect('sale_list')
        return render(request, 'sale_form.html', {'form': form})

class SaleUpdateView(View):
    def get(self, request, pk):
        sale = get_object_or_404(Sale, pk=pk)
        form = SaleForm(instance=sale)
        return render(request, 'sale_form.html', {'form': form})
    
    def post(self, request, pk):
        sale = get_object_or_404(Sale, pk=pk)
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
        return render(request, 'sale_form.html', {'form': form})

class SaleDeleteView(View):
    def get(self, request, pk):
        sale = get_object_or_404(Sale, pk=pk)
        return render(request, 'sale_confirm_delete.html', {'sale': sale})
    
    def post(self, request, pk):
        sale = get_object_or_404(Sale, pk=pk)
        # Note: Deleting a sale doesn't restore stock (keep simple for now)
        sale.delete()
        return redirect('sale_list')