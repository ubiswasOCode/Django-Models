
from django.contrib import admin

from Ecommapp.models import Product, RegisterUser, Category

# Register your models here.
admin.site.register(RegisterUser)
admin.site.register(Product)
admin.site.register(Category)
