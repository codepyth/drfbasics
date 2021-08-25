from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    product_code = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Whishlist(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id.name +" "+ self.customer_id.name
