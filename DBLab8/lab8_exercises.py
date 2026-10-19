
from datetime import datetime
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


# Exercise 7
def exercise_7():
    print("--- Exercise 7 ---")
    for o in db.orders.find({"items.product_id": 2}):
        # print(o)
        print("Order:", o["_id"])


# Exercise 8
def exercise_8():
    print("--- Exercise 8 ---")
    result = db.products.update_many({"category": "Accessories"}, {"$inc": {"price": 20}})
    print(result.modified_count, "product prices have been changed.")
    for p in db.products.find({"category": "Accessories"}):
        print(p["name"], p["price"])


# Exercise 9
def exercise_9():
    print("--- Exercise 9 ---")
    result = db.products.update_one(
        {"name": "Rain Jacket"}, 
        {
            "$addToSet": {"tags": "new"}, 
            "$set": {"restock_date": datetime.now()}
        }
    )
    print(result.modified_count, "products have been modified.")
    print(db.products.find_one({"name": "Rain Jacket"}))


# Exercise 10
def exercise_10():
    print("--- Exercise 10 ---")
    flt = {"status": "new", "order_date": {"$lt": datetime(2026, 3, 20)}}
    print(db.orders.count_documents(flt))
    result = db.orders.delete_many(flt)
    print(result.deleted_count)


# Running exercises
if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    # The exercise_8 will add 20 to the products in "Accessories" every time it's run,
    # and the exercise_9 will modify the "restock_date" field every time it's run.
    # Repeating exercise_10 will just return 0's.
    # exercise_8()
    # exercise_9()
    # exercise_10()
