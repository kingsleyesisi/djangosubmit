from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Product name, e.g., "Laptop"
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price, e.g., 999.99
    stock = models.IntegerField(default=0)  # Available quantity

    def __str__(self):
        return self.name  # Displays name in admin panel

class Customer(models.Model):
    name = models.CharField(max_length=100)  # Customer name, e.g., "John Doe"
    email = models.EmailField(unique=True)  # Unique email
    phone = models.CharField(max_length=15, blank=True)  # Optional phone

    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to Product
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Link to Customer
    quantity = models.IntegerField(default=1)  # Quantity sold
    sale_date = models.DateTimeField(auto_now_add=True)  # Automatically set to now
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Calculated field

    def save(self, *args, **kwargs):
        # Simple logic: Calculate total price before saving
        self.total_price = self.product.price * self.quantity
        # Update stock (subtract quantity sold)
        self.product.stock -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return f"Sale of {self.quantity} {self.product.name} to {self.customer.name}"