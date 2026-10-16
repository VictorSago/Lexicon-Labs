
from pymongo import MongoClient
from pprint import pprint


client = MongoClient("mongodb://localhost:27017/")

db = client["webshop"]


# Exercise 1
def exercise_1():
    print("--- Exercise 1 ---")
    for product in db.products.find({"category": "Accessories"}):
        print(product["name"])


# Exercise 2
def exercise_2():
    print("--- Exercise 2 ---")
    for customer in db.customers.find({"city": "Göteborg"}):
        print(customer["first_name"], customer["last_name"])


# Exercise 3
def exercise_3():
    print("--- Exercise 3 ---")
    for product in db.products.find():
        print(f"{product['name']:<20} {product['price']:>10.2f}")


# Exercise 4
def exercise_4():
    print("--- Exercise 4 ---")
    city_name = "Uppsala"
    print(f"{db.customers.count_documents({'city': city_name})} customer live in {city_name}")


# Exercise 5
def exercise_5():
    print("--- Exercise 5 ---")
    prod_name = "Sandals"
    product = db.products.find_one({"name": prod_name})
    stock = product['stock'] if product is not None else 0
    print(f"There are {stock} units of {prod_name} in stock.")


# Exercise 6
def exercise_6():
    print("--- Exercise 6 ---")
    for customer in db.customers.find({"newsletter": True}):
        print(customer["first_name"])


# Exercise 7
def exercise_7():
    print("--- Exercise 7 ---")
    to_insert = {
        "first_name": "Vic",
        "last_name": "Sago",
        "email": "vic.s@example.com",
        "city": "Stockholm"
    }
    result = db.customers.insert_one(to_insert)
    print("Inserted _id:", result.inserted_id)
    me = db.customers.find_one({"email": to_insert["email"]})
    pprint(me)


# Exercise 8
def exercise_8():
    print("--- Exercise 8 ---")
    db.products.insert_many(
        [
            {
                "_id": 13, 
                "name": "Scarf", 
                "category": "Accessories", 
                "price": 229, 
                "stock": 15, 
                "tags": ["winter", "wool"]
                },
            {
                "_id": 14, 
                "name": "Sunglasses", 
                "category": "Accessories", 
                "price": 299, 
                "stock": 20, 
                "tags": ["summer"]}
        ]
    )
    print(f"There are {db.products.count_documents({})} products in thewebshp.")


# Running exercises
if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    # exercise_7()
    # exercise_8()
