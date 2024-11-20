from django.db import models
from django.shortcuts import get_object_or_404
# Create your models here.

# 1st model============


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
        # return get_object_or_404(Category)
    
    def __str__(self):
        return self.name


# 2nd model===============
'''
class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1) #category_id-1
    description = models.CharField(max_length=300,blank=True,null=True,default='')
    image = models.ImageField(upload_to='uploads/products')

    @staticmethod
    def get_product_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Products.objects.filter(category_id)
        else:
            return Products.get_all_products()
'''
# It includes methods for retrieving products by specific IDs,
# fetching all products,
# and filtering products by category ID.
class Products(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='uploads/products/')

    # category: A ForeignKey
    # field linking each product to a Category.
    # on_delete = models.CASCADE
    # means that if the associated category is deleted,
    # all products in that category will also be deleted.

    @staticmethod
    def get_products_by_id(ids):
         return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products();

#  3rd models===========


class Customer(models.Model):
    id = models.BigAutoField(primary_key = True )
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False


#  4td models===========
import datetime


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.DecimalField(max_digits=10,decimal_places=2 ) # Better for currency
    phone = models.CharField(max_length=10,blank=True,default='')
    address = models.CharField(max_length=50,default = '',blank =True)
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default=False)

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')





