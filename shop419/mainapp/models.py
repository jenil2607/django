from django.db import models

# Create your models here.

# ant time we make any changea in the class definations, espacially hte variables,
# we need to run tow commands.
# 

class Product(models.Model):
    # list out all the project variables below and intialize with certian Classes.

    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(null=False)
    desc = models.TextField()
    pic = models.ImageField(upload_to="products/", null = False)
    stock = models.PositiveBigIntegerField(default = 1)