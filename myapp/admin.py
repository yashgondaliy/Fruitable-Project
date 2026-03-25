from django.contrib import admin
from .models import*
# Register your models here.

admin.site.register(user)
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Add_to_cart)
admin.site.register(Add_to_wishlist)
admin.site.register(Billing_details)
admin.site.register(user_coupon)
admin.site.register(Coupon)
admin.site.register(Orders)


