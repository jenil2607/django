from django.db import models
from mainapp.models import Product
from django.contrib.auth.models import User


# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"product: {self.product.name} - Count: {self.quantity}"
    def get_total_price(self):
        return self.quantity * self.product.price
        