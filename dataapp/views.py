from django.http import HttpResponse
from django.shortcuts import render
from threading import Thread
from .models import User, Product, Order

users_data = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"},
    {"name": "David", "email": "david@example.com"},
    {"name": "Eve", "email": "eve@example.com"},
    {"name": "Frank", "email": "frank@example.com"},
    {"name": "Grace", "email": "grace@example.com"},
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Henry", "email": "henry@example.com"},
    {"name": None, "email": "jane@example.com"},
]

products_data = [
    {"name": "Laptop", "price": 1000.00},
    {"name": "Smartphone", "price": 700.00},
    {"name": "Headphones", "price": 150.00},
    {"name": "Monitor", "price": 300.00},
    {"name": "Keyboard", "price": 50.00},
    {"name": "Mouse", "price": 30.00},
    {"name": "Laptop", "price": 1000.00},
    {"name": "Smartwatch", "price": 250.00},
    {"name": "Gaming Chair", "price": 500.00},
    {"name": "Earbuds", "price": -50.00},
]

orders_data = [
    {"user_id": 1, "product_id": 1, "quantity": 2},
    {"user_id": 2, "product_id": 2, "quantity": 1},
    {"user_id": 3, "product_id": 3, "quantity": 5},
    {"user_id": 4, "product_id": 4, "quantity": 1},
    {"user_id": 5, "product_id": 5, "quantity": 3},
    {"user_id": 6, "product_id": 6, "quantity": 4},
    {"user_id": 7, "product_id": 7, "quantity": 2},
    {"user_id": 8, "product_id": 8, "quantity": 0},
    {"user_id": 9, "product_id": 1, "quantity": -1},
    {"user_id": 10, "product_id": 11, "quantity": 2},
]


def insert_users():
    print("Inserting Users:")
    for user in users_data:
        User.objects.create(**user)
        print(f"Inserted: {user}")
    print("Users inserted successfully!")


def insert_products():
    print("Inserting Products:")
    for product in products_data:
        Product.objects.create(**product)
        print(f"Inserted: {product}")
    print("Products inserted successfully!")


def insert_orders():
    print("Inserting Orders:")
    for order in orders_data:
        Order.objects.create(
            user_id=order["user_id"],
            product_id=order["product_id"],
            quantity=order["quantity"],
        )
        print(f"Inserted: {order}")
    print("Orders inserted successfully!")

def insert_data(request):
 
    user_thread = Thread(target=insert_users)
    product_thread = Thread(target=insert_products)
    order_thread = Thread(target=insert_orders)

 
    user_thread.start()
    product_thread.start()
    order_thread.start()

   
    user_thread.join()
    product_thread.join()
    order_thread.join()

  
    return HttpResponse("All data inserted successfully!")

