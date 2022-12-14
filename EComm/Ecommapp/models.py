from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class RegisterUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, default='')
    email = models.EmailField()
    
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)

    # def __str__(self):
    #     return self.first_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', related_name='category', on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=200,default='',null=True )
    brand = models.CharField(max_length=200,default='',null=True )
    description = models.TextField(default='', null=True )
    # # price = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default="0.00")

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=20, default='',)

    def __str__(self):
        return self.name

