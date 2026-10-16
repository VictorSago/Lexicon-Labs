
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


# Exercise 3
def exercise_3():
    print("--- Exercise 3 ---")
    for c in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
        print(f"{c['first_name']} {c['last_name']} ({c['city']})")


# Exercise 4
def exercise_4():
    print("--- Exercise 4 ---")
    for p in db.products.find({"details.color": "white"}):
        print(f"{p['_id']} {p['name']}")


# Exercise 5
def exercise_5():
    print("--- Exercise 5 ---")
    for p in db.products.find({"tags": "sport"}, {"name": 1, "tags": 1, "_id": 0}):
        #print(p)
        print(f"{p['name']}, Tags: {p['tags']}")


# Exercise 6
def exercise_6():
    print("--- Exercise 6 ---")
    for p in db.products.find({}, {"name": 1, "price": 1, "_id": 0}).sort("price", 1).limit(5):
        print(p)


# Running exercises
if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
