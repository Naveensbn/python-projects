from django.contrib import admin
from store.models import Category
from store.models import Products
from store.models import Customer
from store.models import Order

class CategoryAdmin(admin.ModelAdmin):
    # list = ['name']
    list_display = ['name']


class ProductsAdmin(admin.ModelAdmin):
    # list = ['name','price','category','image','description',]
    list_display = ['name', 'price', 'category']

admin.site.register(Products,ProductsAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)


# Register your models here.

# Username (leave blank to use 'navee'): admin
# Email address: admin@gmail.com
# Password: admin
