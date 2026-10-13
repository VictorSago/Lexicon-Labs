"""Creates (or resets) the webshop database in MongoDB.
Run it with:  python seed_webshop.py
WARNING: deletes the customers, products and orders collections first."""
from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

customers = [
    {"_id": 1, "first_name": "Anna", "last_name": "Lindqvist", "email": "anna.lindqvist@example.com", "city": "Uppsala", "joined": datetime(2024, 3, 14), "newsletter": True},
    {"_id": 2, "first_name": "Erik", "last_name": "Johansson", "email": "erik.j@example.com", "city": "Stockholm", "joined": datetime(2023, 11, 2), "phone": "070-1234567"},
    {"_id": 3, "first_name": "Sara", "last_name": "Ahmed", "email": "sara.ahmed@example.com", "city": "Göteborg", "joined": datetime(2025, 1, 20), "newsletter": True},
    {"_id": 4, "first_name": "Johan", "last_name": "Berg", "email": "johan.berg@example.com", "city": "Uppsala", "joined": datetime(2022, 6, 30)},
    {"_id": 5, "first_name": "Maria", "last_name": "Nilsson", "email": "maria.n@example.com", "city": "Malmö", "joined": datetime(2025, 8, 11), "phone": "073-7654321"},
    {"_id": 6, "first_name": "Ali", "last_name": "Hassan", "email": "ali.hassan@example.com", "city": "Stockholm", "joined": datetime(2024, 9, 5), "newsletter": False},
    {"_id": 7, "first_name": "Emma", "last_name": "Karlsson", "email": "emma.k@example.com", "city": "Västerås", "joined": datetime(2023, 2, 17)},
    {"_id": 8, "first_name": "Oskar", "last_name": "Persson", "email": "oskar.p@example.com", "city": "Uppsala", "joined": datetime(2025, 5, 28), "newsletter": True},
    {"_id": 9, "first_name": "Fatima", "last_name": "Yilmaz", "email": "fatima.y@example.com", "city": "Göteborg", "joined": datetime(2024, 12, 1), "phone": "076-1112233"},
    {"_id": 10, "first_name": "Lukas", "last_name": "Ek", "email": "lukas.ek@example.com", "joined": datetime(2026, 1, 9)}
]

products = [
    {"_id": 1, "name": "Hoodie Black", "category": "Clothing", "price": 599, "stock": 25, "tags": ["winter", "cotton", "bestseller"], "details": {"color": "black", "material": "cotton"}},
    {"_id": 2, "name": "T-shirt White", "category": "Clothing", "price": 249, "stock": 60, "tags": ["summer", "cotton"], "details": {"color": "white", "material": "cotton"}},
    {"_id": 3, "name": "Cap Logo", "category": "Accessories", "price": 199, "stock": 40, "tags": ["summer"], "details": {"color": "black"}},
    {"_id": 4, "name": "Sneakers Classic", "category": "Shoes", "price": 1199, "stock": 12, "tags": ["bestseller"], "details": {"color": "white", "material": "leather"}, "sizes": [39, 40, 41, 42, 43, 44]},
    {"_id": 5, "name": "Water Bottle", "category": "Accessories", "price": 149, "stock": 0, "tags": ["sport"], "details": {"color": "green", "material": "steel"}},
    {"_id": 6, "name": "Joggers Grey", "category": "Clothing", "price": 499, "stock": 18, "tags": ["sport", "cotton"], "details": {"color": "grey", "material": "cotton"}},
    {"_id": 7, "name": "Backpack Urban", "category": "Accessories", "price": 749, "stock": 8, "tags": ["travel"], "details": {"color": "black", "material": "nylon"}},
    {"_id": 8, "name": "Running Shoes", "category": "Shoes", "price": 1399, "stock": 5, "tags": ["sport", "bestseller"], "details": {"color": "blue"}, "sizes": [40, 41, 42, 43, 44, 45]},
    {"_id": 9, "name": "Socks 3-pack", "category": "Clothing", "price": 129, "stock": 100, "tags": ["cotton"], "details": {"color": "white", "material": "cotton"}},
    {"_id": 10, "name": "Beanie", "category": "Accessories", "price": 179, "stock": 30, "tags": ["winter"], "details": {"color": "black", "material": "wool"}},
    {"_id": 11, "name": "Rain Jacket", "category": "Clothing", "price": 1299, "stock": 0, "tags": ["winter", "waterproof"], "details": {"color": "yellow", "material": "polyester"}},
    {"_id": 12, "name": "Sandals", "category": "Shoes", "price": 399, "stock": 22, "tags": ["summer"], "details": {"color": "brown", "material": "leather"}, "sizes": [37, 38, 39, 40, 41]}
]

orders = [
    {"_id": 1, "customer_id": 1, "order_date": datetime(2026, 1, 5), "status": "delivered", "items": [{"product_id": 1, "name": "Hoodie Black", "quantity": 1, "unit_price": 599}, {"product_id": 3, "name": "Cap Logo", "quantity": 2, "unit_price": 199}]},
    {"_id": 2, "customer_id": 2, "order_date": datetime(2026, 1, 12), "status": "delivered", "items": [{"product_id": 4, "name": "Sneakers Classic", "quantity": 1, "unit_price": 1199}]},
    {"_id": 3, "customer_id": 1, "order_date": datetime(2026, 1, 20), "status": "delivered", "items": [{"product_id": 9, "name": "Socks 3-pack", "quantity": 3, "unit_price": 129}]},
    {"_id": 4, "customer_id": 3, "order_date": datetime(2026, 1, 28), "status": "delivered", "items": [{"product_id": 2, "name": "T-shirt White", "quantity": 2, "unit_price": 249}, {"product_id": 6, "name": "Joggers Grey", "quantity": 1, "unit_price": 499}]},
    {"_id": 5, "customer_id": 4, "order_date": datetime(2026, 2, 3), "status": "delivered", "items": [{"product_id": 8, "name": "Running Shoes", "quantity": 1, "unit_price": 1399}]},
    {"_id": 6, "customer_id": 5, "order_date": datetime(2026, 2, 10), "status": "delivered", "items": [{"product_id": 1, "name": "Hoodie Black", "quantity": 1, "unit_price": 599}, {"product_id": 10, "name": "Beanie", "quantity": 1, "unit_price": 179}]},
    {"_id": 7, "customer_id": 6, "order_date": datetime(2026, 2, 14), "status": "cancelled", "items": [{"product_id": 7, "name": "Backpack Urban", "quantity": 1, "unit_price": 749}]},
    {"_id": 8, "customer_id": 2, "order_date": datetime(2026, 2, 21), "status": "delivered", "items": [{"product_id": 2, "name": "T-shirt White", "quantity": 1, "unit_price": 249}, {"product_id": 9, "name": "Socks 3-pack", "quantity": 2, "unit_price": 129}]},
    {"_id": 9, "customer_id": 8, "order_date": datetime(2026, 2, 27), "status": "shipped", "items": [{"product_id": 11, "name": "Rain Jacket", "quantity": 1, "unit_price": 1299}]},
    {"_id": 10, "customer_id": 9, "order_date": datetime(2026, 3, 4), "status": "shipped", "items": [{"product_id": 3, "name": "Cap Logo", "quantity": 1, "unit_price": 199}, {"product_id": 2, "name": "T-shirt White", "quantity": 3, "unit_price": 249}]},
    {"_id": 11, "customer_id": 1, "order_date": datetime(2026, 3, 9), "status": "shipped", "items": [{"product_id": 6, "name": "Joggers Grey", "quantity": 2, "unit_price": 499}]},
    {"_id": 12, "customer_id": 3, "order_date": datetime(2026, 3, 15), "status": "new", "items": [{"product_id": 4, "name": "Sneakers Classic", "quantity": 1, "unit_price": 1199}, {"product_id": 9, "name": "Socks 3-pack", "quantity": 1, "unit_price": 129}]},
    {"_id": 13, "customer_id": 6, "order_date": datetime(2026, 3, 18), "status": "new", "items": [{"product_id": 1, "name": "Hoodie Black", "quantity": 2, "unit_price": 599}]},
    {"_id": 14, "customer_id": 4, "order_date": datetime(2026, 3, 22), "status": "new", "items": [{"product_id": 10, "name": "Beanie", "quantity": 2, "unit_price": 179}, {"product_id": 3, "name": "Cap Logo", "quantity": 1, "unit_price": 199}]},
    {"_id": 15, "customer_id": 2, "order_date": datetime(2026, 3, 28), "status": "new", "items": [{"product_id": 8, "name": "Running Shoes", "quantity": 1, "unit_price": 1399}, {"product_id": 2, "name": "T-shirt White", "quantity": 1, "unit_price": 249}]}
]

for name in ["customers", "products", "orders"]:
    db[name].drop()

db.customers.insert_many(customers)
db.products.insert_many(products)
db.orders.insert_many(orders)

print("webshop is ready:",
      db.customers.count_documents({}), "customers,",
      db.products.count_documents({}), "products,",
      db.orders.count_documents({}), "orders")
