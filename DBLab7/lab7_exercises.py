
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
