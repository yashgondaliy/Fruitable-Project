# 🛒 Fruitable - Django E-commerce Project

A fully functional **E-commerce Web Application** built using **Django**.
This project allows users to browse products, add items to cart, manage wishlist, and place orders.

---

## 🚀 Features

### 👤 User Features

* User Registration & Login system
* Secure session-based authentication
* Logout functionality

### 🛍️ Product Features

* Product listing (Fruits & Vegetables)
* Product detail view
* Category-based filtering
* Price display

### 🛒 Cart System

* Add to cart
* Increase / Decrease quantity
* Remove items from cart
* Total price calculation

### ❤️ Wishlist

* Add to wishlist
* Remove from wishlist

### 📦 Orders

* Place order
* View order history
* Delete orders

### 🎟️ Coupon System

* Apply coupon codes
* Discount calculation
* Expiry handling

### 💳 Checkout

* Billing details form
* Address management

### 📞 Contact

* Contact form for user queries

---

## 🛠️ Tech Stack

| Technology      | Description           |
| --------------- | --------------------- |
| Python          | Backend language      |
| Django          | Web framework         |
| HTML            | Structure             |
| CSS / Bootstrap | Styling               |
| JavaScript      | Frontend interactions |
| SQLite          | Database              |

---

## 📁 Project Structure

```
myproject/
│
├── myapp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── media/
├── db.sqlite3
├── manage.py
├── README.md
```

---

## ⚙️ Installation Guide

### 🔹 1. Clone Repository

```
git clone https://github.com/yashgondaliya/Fruitable-Project.git
cd Fruitable-Project
```

---

### 🔹 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate     # Windows
```

---

### 🔹 3. Install Dependencies

```
pip install django
```

---

### 🔹 4. Apply Migrations

```
python manage.py migrate
```

---

### 🔹 5. Run Server

```
python manage.py runserver
```

---

### 🔹 6. Open in Browser

```
http://127.0.0.1:8000/
```

---

## 🔑 Key Functionalities

* Dynamic product loading
* Session-based user management
* Cart stored per user
* Order tracking system
* Coupon validation logic

---

## 📸 Screenshots 

### 🏠 Home Page
![Home Page](screenshots/home.png)

### 🛍️ Shop Page
![Cart](screenshots/cart.png)

### 🛒 Cart Page
![Cart](screenshots/cart.png)

### 💳 Checkout Page
![Cart](screenshots/cart.png)

---

## 🧠 Learning Outcomes

* Django MVC (Model-View-Template)
* Database relationships
* Session handling
* CRUD operations
* Frontend + Backend integration

---

## 📌 Future Improvements

* 🔥 AJAX Add to Cart (no page reload)
* 💳 Payment Gateway Integration (Razorpay/Stripe)
* 📊 Admin Dashboard
* 📱 Responsive UI improvements
* 🔐 Django Authentication System upgrade

---

## ⚠️ Notes

* `db.sqlite3` should not be uploaded in production
* Use `.gitignore` to exclude unnecessary files

---

## 🧑‍💻 Author

**Yash Gondaliya**

---

## ⭐ Support

If you like this project:

👉 Give it a ⭐ on GitHub
👉 Share with your friends

---

## 📬 Contact

For queries or suggestions, feel free to connect.

---

**Thank You ❤️**
