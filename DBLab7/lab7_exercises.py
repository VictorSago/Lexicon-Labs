
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

db = client["webshop"]


# Exercise 1
print("--- Exercise 1 ---")
for product in db.products.find({"category": "Accessories"}):
    print(product["name"])


# Exercise 2
print("--- Exercise 2 ---")
for customer in db.customers.find({"city": "Göteborg"}):
    print(customer["first_name"], customer["last_name"])


# Exercise 3
print("--- Exercise 3 ---")
for product in db.products.find():
    print(f"{product['name']:<20} {product['price']:>10.2f}")


# Exercise 4
print("--- Exercise 4 ---")
city_name = "Uppsala"
print(f"{db.customers.count_documents({'city': city_name})} customer live in {city_name}")


# Exercise 5
print("--- Exercise 5 ---")
prod_name = "Sandals"
product = db.products.find_one({"name": prod_name})
stock = product['stock'] if product is not None else 0
print(f"There are {stock} units of {prod_name} in stock.")


# Exercise 6
print("--- Exercise 6 ---")
for customer in db.customers.find({"newsletter": True}):
    print(customer["first_name"])
