"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('shop_detail', views.shop_detail, name='shop_detail'),
    path('shop_detail1/<int:id>', views.shop_detail1, name='shop_detail1'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('cart', views.cart, name='cart'),
    path('add_cart/<int:id>', views.add_cart, name='add_cart'),
    path('quantity_plus/<int:id>', views.quantity_plus, name='quantity_plus'),
    path('quantity_minus/<int:id>', views.quantity_minus, name='quantity_minus'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item'),
    path('contact', views.contact, name='contact'),
    path('error', views.error, name='error'),
    path('chackout', views.chackout, name='chackout'),
    path('billing_add', views.billing_add, name='billing_add'),
    path('apply_coupon', views.apply_coupon, name='apply_coupon'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('forget_pass', views.forget_pass, name='forget_pass'),
    path('price_filter', views.price_filter, name='price_filter'),
    path('wishlist', views.wishlist, name='wishlist'),  
    path('orders', views.orders, name='orders'),  
    path('delete_orders/<int:id>', views.delete_orders, name='delete_orders'),
    path('add_wish/<int:id>', views.add_wish, name='add_wish'),
    path('delete_wishlist/<int:id>', views.delete_wishlist, name='delete_wishlist'),

    


]
