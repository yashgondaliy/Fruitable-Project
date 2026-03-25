from django.db import models
from .models import*

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    email=models.EmailField(unique=True,blank=True,null=True)
    password=models.CharField(max_length=128,blank=True,null=True)
    # con_password=models.CharField(blank=True,null=True)

    def __str__(self):
        return self.name
    
class Categories(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    cate_id=models.ForeignKey(Categories,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=255,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    dec=models.TextField()
    price=models.IntegerField()

    def __str__(self):
        return self.name
    

    
class Add_to_cart(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    name=models.CharField(max_length=255,blank=True,null=True)
    price=models.IntegerField()
    quantity=models.IntegerField()
    total_price=models.IntegerField()

    def __str__(self):
        return self.name


class Add_to_wishlist(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    Product_id=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    name=models.CharField(max_length=250,blank=True,null=True)
    price=models.IntegerField()

    def __str__(self):
        return self.name
    
class Billing_details(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    first_name=models.CharField(max_length=255,blank=True,null=True)
    last_name=models.CharField(max_length=255,blank=True,null=True)
    company_name=models.CharField(max_length=255,blank=True,null=True)
    address=models.TextField(max_length=255,blank=True,null=True)
    city=models.CharField(max_length=255,blank=True,null=True)
    country=models.CharField(max_length=255,blank=True,null=True)
    pincode=models.IntegerField(blank=True,null=True)
    mobile=models.IntegerField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    note=models.TextField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.first_name

class Coupon(models.Model):
    coupon_code=models.CharField(max_length=255,blank=True,null=True)
    discount=models.IntegerField()
    expiry_time=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.coupon_code

class user_coupon(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    coupon_id=models.ForeignKey(Coupon,on_delete=models.CASCADE,blank=True,null=True)
    ex=models.BooleanField(blank=True,null=True)
    expiry_time=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.coupon_id.coupon_code
    
class Orders(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    name=models.CharField(max_length=255,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    date_time=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    quantity=models.IntegerField(blank=True,null=True)
    total_price=models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=255,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    message=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name



    


        

