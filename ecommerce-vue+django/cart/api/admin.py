from django.contrib import admin

# Register your models here.
from .models import Product,cart
admin.site.register(Product)
admin.site.register(cart)
