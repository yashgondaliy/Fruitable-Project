from pyexpat.errors import messages
from django.shortcuts import render,HttpResponse,redirect
from .models import*
from django.core.paginator import Paginator
import razorpay
# Create your views here.
from django.contrib import messages

def home(request):
    return HttpResponse("name:- yash, pass:- yash")

def index(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session["email"])
        p_id=Product.objects.order_by('?')[:8]
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        wish_count=Add_to_wishlist.objects.filter(user_id=uid).count()

        fruits_id=Categories.objects.filter(name__iexact='Fruits').first()
        if fruits_id:
            fruits=Product.objects.filter(cate_id=fruits_id)
        else:
            fruits=[]

        vegetable_category = Categories.objects.filter(name__iexact='vegetables').first()
        if vegetable_category:
            vegetables = Product.objects.filter(cate_id=vegetable_category)
        else:
            vegetables = []

        con={"user_id":uid,"p_id":p_id,"cart_count":cart_count,"wish_count":wish_count,"fruits":fruits,"vegetables":vegetables}
        return render(request,"index.html",con)
    else:
        return render(request,"login.html")

def shop(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session["email"])

        cid = Categories.objects.all()
        category_id = request.GET.get('category')
        wish_count=Add_to_wishlist.objects.filter(user_id=uid).count()
        p_id = Product.objects.all().order_by("-id")
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        wishlist_product=Add_to_wishlist.objects.filter(user_id=uid)
        l1=[]
        for i in wishlist_product:
            l1.append(i.Product_id.id)

        if category_id:
            p_id = Product.objects.filter(cate_id=category_id)
        else:
            p_id = Product.objects.all().order_by("-id")


        paginator = Paginator(p_id,3)
        page_number = request.GET.get("page",1)
        p_id = paginator.get_page(page_number)
        show_page = paginator.get_elided_page_range(page_number,on_each_side=2,on_ends=2)
        
        con = {"l1":l1,"user_id":uid,"wishlist_product":wishlist_product,"cid": cid, "p_id": p_id,"cart_count":cart_count,"show_page":show_page,"wish_count":wish_count}
        return render(request, "shop.html", con)
    return render(request,"login.html")

def shop_detail1(request,id):
    p_id = Product.objects.get(id=id)
    cart_count=Add_to_cart.objects.all().count()

    con={ "p_id": p_id,"cart_count":cart_count}
    return render(request,"shop_detail.html",con)

def shop_detail(request):
    cart_count=Add_to_cart.objects.all().count()
    con={"cart_count":cart_count}
    return render(request,"shop_detail.html",con)

def price_filter(request):
    if request.POST:
        max1=request.POST["max1"]
        p_id = Product.objects.filter(price__lte=max1)
        con={"p_id":p_id,"max1":max1}
    return render(request,"shop.html",con)

def testimonial(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session["email"])
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        wish_count=Add_to_wishlist.objects.filter(user_id=uid).count()
        con={"user_id":uid,"cart_count":cart_count,"wish_count":wish_count}
        return render(request,"testimonial.html",con)
    return render(request,"login.html")

def cart(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session["email"])
        cart_item=Add_to_cart.objects.filter(user_id=uid)
        wish_count=Add_to_wishlist.objects.filter(user_id=uid).count()
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()

        ucid=user_coupon.objects.filter(user_id=uid,ex=True).order_by("-id").first()

        total_price=0
        for i in cart_item:
            total_price += i.product_id.price * i.quantity

        shipping_charge=50

        if total_price==0:
            shipping_charge==0
        else:
            shipping_charge=50
        
        if ucid == None:
            discount=0
        else:
            discount=ucid.coupon_id.discount
            total_price -= ucid.coupon_id.discount
            print(ucid.coupon_id.discount)

        if cart_item.count() == 0 and ucid != None:
            ucid.ex=False
            discount=0
            total_price=0
            ucid.save()

        grand_total=total_price+shipping_charge-discount
            


        con={"user_id": uid,"discount":discount,"cart_item":cart_item,"cart_count":cart_count,"total_price":total_price,"grand_total":grand_total,"shipping_charge":shipping_charge,"wish_count":wish_count}

        return render(request,"cart.html",con)
    return render(request,"login.html")

def add_cart(request,id):
    if 'email' in request.session:
        pid=Product.objects.get(id=id)
        uid=user.objects.get(email=request.session["email"])
        cart_item=Add_to_cart.objects.filter(product_id=pid,user_id=uid).first()
        if cart_item:
            cart_item.quantity += 1
            cart_item.total_price = cart_item.quantity * cart_item.price
            cart_item.save()
        
        else:
            Add_to_cart.objects.create(user_id=uid,product_id=pid,image=pid.image,name=pid.name,price=pid.price,quantity=1,total_price=pid.price)
        
        return redirect("shop")
    else:
        return render(request,"login.html")

def quantity_plus(request,id):

    cart_item=Add_to_cart.objects.get(id=id)
    if cart_item:
        cart_item.quantity += 1
        cart_item.total_price = cart_item.quantity * cart_item.price
        cart_item.save()
        return redirect("cart")
    
    else:
        return redirect("cart")
    
def quantity_minus(request,id):
    cart_item=Add_to_cart.objects.get(id=id)
    
    if cart_item:
        if (cart_item.quantity==1):
            Add_to_cart.objects.get(id=id).delete()
            
        else:
            cart_item.quantity -= 1
            cart_item.total_price = cart_item.quantity * cart_item.price
            cart_item.save()
            return redirect("cart")
        
        return redirect("cart")
    
    else:    
        return redirect("cart")

def delete_item(request,id):
    dell=Add_to_cart.objects.filter(id=id)
    dell.delete()
    return redirect("cart")

def chackout(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session["email"])

        chack_id=Add_to_cart.objects.filter(user_id=uid)
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        wish_count=Add_to_wishlist.objects.filter(user_id=uid).count()
        ucid=user_coupon.objects.filter(user_id=uid,ex=True).order_by("-id").first()
        total_price=0
        for i in chack_id:
            total_price += i.product_id.price * i.quantity
        
        shipping_charge=50

        if total_price == 0:
            shipping_charge == 0
        else:
            shipping_charge == 50
        
        discount = 0

        if ucid:
            discount = ucid.coupon_id.discount
        
        grand_total = total_price + shipping_charge - discount

        client = razorpay.Client(auth=('rzp_test_uqhoYnBzHjbvGF', 'jEhBs6Qp9hMeGfq5FyU45cVi'))
        response = client.order.create({
            'amount': int(grand_total * 100),
            'currency': 'INR',
            'payment_capture': 1
        })
        print("Razorpay response:", response)
            

        con={"user_id": uid,"chack_id":chack_id,"cart_count":cart_count,"wish_count":wish_count,"ucid":ucid,"total_price":total_price,"shipping_charge":shipping_charge,"grand_total":grand_total,"discount":discount,"response":response}

        return render(request,"chackout.html",con)
    return render(request,"login.html")

# def billing_add(request):
#     if "email" in request.session and request.method=="POST":
#         uid = user.objects.get(email=request.session["email"])
#         if request.POST:
#             first_name=request.POST["first_name"]
#             last_name=request.POST["last_name"]
#             company_name=request.POST["company_name"]
#             address=request.POST["address"]
#             city=request.POST["city"]
#             country=request.POST["country"]
#             pincode=request.POST["pincode"]
#             mobile=request.POST["mobile"]
#             email=request.POST["email"]
#             note=request.POST["note"]

#             if first_name and last_name and company_name and address and city and country and pincode and mobile and email and note:

#                 Billing_details.objects.create(first_name=first_name,
#                                             last_name=last_name,
#                                             company_name=company_name,
#                                             address=address,
#                                             city=city,
#                                             country=country,
#                                             pincode=pincode,
#                                             mobile=mobile,
#                                             email=email,
#                                             note=note)
#                 return redirect(chackout)
#             return render(request,"chackout.html")
#         else:
#             return render(request,"chackout.html")

from django.shortcuts import render, redirect
from .models import user, Orders, Add_to_cart, Billing_details
from django.utils import timezone

def billing_add(request):
    if "email" in request.session and request.method == "POST":
        uid = user.objects.get(email=request.session["email"])

        Billing_details.objects.create(
            user_id=uid,
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            company_name=request.POST.get("company_name"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            country=request.POST.get("country"),
            pincode=request.POST.get("pincode"),
            mobile=request.POST.get("mobile"),
            email=request.POST.get("email"),
            note=request.POST.get("note"),
        )

        cart_items = Add_to_cart.objects.filter(user_id=uid)
        for item in cart_items:
            Orders.objects.create(
                user_id=uid,
                image=item.image,
                name=item.name,
                price=item.price,
                quantity=item.quantity,
                total_price=item.total_price,
                date_time=timezone.now()
            )

        cart_items.delete()

        return redirect("orders")

    return redirect("checkout")


def apply_coupon(request):
    uid=user.objects.get(email=request.session["email"])
    if request.POST:
        coupon_code=request.POST.get('code')

        ccid=Coupon.objects.filter(coupon_code=coupon_code).exists()

        if ccid:
            ccid1=Coupon.objects.get(coupon_code=coupon_code)
            ucid=user_coupon.objects.filter(user_id=uid,coupon_id=ccid1,ex=True).exists()
            if ucid:
                messages.info(request,"You have already used this Coupon")
                return redirect("cart")
            else:
                user_coupon.objects.create(user_id=uid,coupon_id=ccid1,ex=True)
                messages.success(request,"Coupon applied successfully!")
                return redirect("cart")
        else:
            messages.error(request,"Invalid coupon code.")
            return redirect("cart")
    else:
        return render(request,"cart.html")
    
def contact(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session["email"])
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        wish_count=Add_to_wishlist.objects.filter(user_id=uid).count()
        con={"user_id":uid,"cart_count":cart_count,"wish_count":wish_count}
        if request.POST:
            name=request.POST["name"]
            email=request.POST["email"]
            message=request.POST["message"]

            Contact.objects.create(name=name,email=email,message=message)
            con["msg4"]="submited successfully"
            
            return render(request,"contact.html",con)
        else:
            return render(request,"contact.html",con)
    return render(request,"login.html")

def error(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session["email"])

        cart_count=Add_to_cart.objects.filter(user_id=uid).count()
        wish_count=Add_to_wishlist.objects.filter(user_id=uid).count()
        con={"user_id":uid,"cart_count":cart_count,"wish_count":wish_count}
        return render(request,"error.html",con)
    return render(request,"login.html")

def login(request):
    if 'email' in request.session:
        return render(request,"index.html")
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        try:
            uid=user.objects.get(email=email)
            if uid.password==password:
                # if uid.email==email:
                    request.session['email']=uid.email
                    return redirect("index")
            else:
                con={"msg":"password do not match"}
                return render(request,"login.html",con)
        except:
            con={"msg":"email dose not match any register user" }
            return render(request,"login.html",con)
    else:
        return render(request,"login.html")

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,"login.html")
        
    else:
        return render(request,"login.html")

def register(request):
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        con_password = request.POST["con_password"]

        if con_password==password:
            if user.objects.filter(email=email).exists():
                con={"msg":"email is already registered"}
                return render(request,"register.html",con)
            else:
                user.objects.create(name=name,email=email,password=password)
                return redirect("login")
        else:
            context={"error":"password is not match"}
            return render(request,"register.html",context)


    return render(request, "register.html")


def forget_pass(request):
    return render(request,"forget_pass.html")

import random
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import user  # Your user model

# Temporary OTP storage (use cache or DB in real apps)
otp_storage = {}

def forget_pass(request):
    if request.method == "POST":
        email = request.POST.get("email")
        otp = request.POST.get("otp")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        # Step 1: Email submitted (send OTP)
        if email and not otp:
            try:
                u = user.objects.get(email=email)
                generated_otp = str(random.randint(100000, 999999))
                otp_storage[email] = generated_otp

                # Send OTP
                send_mail(
                    'Your OTP for password reset',
                    f'Your OTP is: {generated_otp}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )

                return render(request, "forget_pass.html", {
                    "msg": "OTP sent to your email",
                    "email_entered": True,
                    "email": email
                })

            except user.DoesNotExist:
                return render(request, "forget_pass.html", {
                    "msg": "Email not registered"
                })

        # Step 2: OTP + password submitted
        elif email and otp and new_password and confirm_password:
            stored_otp = otp_storage.get(email)

            if stored_otp and otp == stored_otp:
                if new_password == confirm_password:
                    u = user.objects.get(email=email)
                    u.password = new_password     # Use hashed password in production
                    u.save()
                    otp_storage.pop(email, None)
                    return redirect("login")
                else:
                    return render(request, "forget_pass.html", {
                        "msg": "Passwords do not match",
                        "email_entered": True,
                        "email": email
                    })
            else:
                return render(request, "forget_pass.html", {
                    "msg": "Invalid OTP",
                    "email_entered": True,
                    "email": email
                })

    return render(request, "forget_pass.html")


def wishlist(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session["email"])

        wish_id=Add_to_wishlist.objects.filter(user_id=uid)
        wish_count=Add_to_wishlist.objects.filter(user_id=uid).count()
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()        
        con={"user_id":uid,"wish_id":wish_id,"wish_count":wish_count,"cart_count":cart_count}
        return render(request,"wishlist.html",con)
    
    return render(request,"wishlist.html")

def add_wish(request, id):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session["email"])
        p_id = Product.objects.get(id=id)

        # Check if the product is already in this user's wishlist
        wish_item = Add_to_wishlist.objects.filter(Product_id=p_id, user_id=uid).first()

        if wish_item:
            wish_item.delete()
        else:
            Add_to_wishlist.objects.create(
                user_id=uid,
                Product_id=p_id,
                image=p_id.image,
                name=p_id.name,
                price=p_id.price
            )
        return redirect("shop")
    else:
        return render(request, "login.html")

    

def delete_wishlist(request,id):

    dell=Add_to_wishlist.objects.get(id=id)
    dell.delete()
    return redirect("wishlist")

def orders(request):
    if "email" in request.session:
        uid=user.objects.get(email=request.session["email"])
        wish_count=Add_to_wishlist.objects.filter(user_id=uid).count()
        cart_count=Add_to_cart.objects.filter(user_id=uid).count()

        order_i=Orders.objects.filter(user_id=uid).order_by("-id")

        con={"wish_count":wish_count,"cart_count":cart_count,"user_id": uid,"order_i":order_i}

        return render(request,"order.html",con)
    else:
        return render(request,"login.html")
    
def delete_orders(request,id):

    dell=Orders.objects.get(id=id)
    dell.delete()
    return redirect("orders")
    

