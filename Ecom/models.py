from django.conf import settings
from django.db import models

# from Ecommerce import settings


class Category(models.Model):
    title=models.CharField(max_length=120)
    def __str__(self):
        return self.title

class Items(models.Model):
    title=models.CharField(max_length=150)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.FloatField()
    description=models.CharField(max_length=200)
    stock=models.IntegerField()
    image = models.ImageField(upload_to="images/")
    date_created=models.DateField(auto_now=True)

    class Meta:
        ordering=['-date_created']
    def __str__(self):
        return self.title

class Mycart(models.Model):
    product=models.ForeignKey(Items,on_delete=models.CASCADE)
    user=models.CharField(max_length=130)
    options = (("cart", "cart"),
               ("orderplaced", "orderplaced"))
    status=models.CharField(max_length=120,choices=options,default="cart")
    def __str__(self):
        return self.product


class Address(models.Model):
    address=models.CharField(max_length=250)
    pincode=models.IntegerField()
    phonenumber=models.IntegerField()

class Orders(models.Model):
    product=models.ForeignKey(Items,on_delete=models.CASCADE)
    user=models.CharField(max_length=120)
    date=models.DateField(auto_now=True)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    def __str__(self):
        return self.product

