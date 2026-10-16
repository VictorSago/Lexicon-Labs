
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

db = client["webshop"]


# Exercise 1
def exercise_1():
    print("--- Exercise 1 ---")
    for p in db.products.find({"price": {"$gt": 1000}}, {"name": 1, "price": 1, "_id": 0}):
        print(f"{p['name']}: {p['price']} kr")


# Exercise 2
def exercise_2():
    print("--- Exercise 2 ---")
    for o in db.orders.find({"status": {"$ne": "delivered"}}, {"status": 1}):
        print(o["_id"], o["status"])


# Running exercises
if __name__ == "__main__":
    exercise_1()
    exercise_2()
