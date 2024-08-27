from django.db import models
from django.contrib.auth.models import User

from .constants import CONDITION_CHOICES, PAYMENT_STATUS_OPTIONS

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.FloatField()
    description = models.TextField()
    condition = models.CharField(max_length=100, choices=CONDITION_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    efficiency = models.FloatField()
    quantity = models.IntegerField()
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/")
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS_OPTIONS, default="unpaid")
    timestamp = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
