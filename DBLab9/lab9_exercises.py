
import json
from pymongo import MongoClient
from pymongo.errors import WriteError


# Exercise 1
# The members would be refrenced, because their information can be shown
# independently of any books. The reviews are a more complex case, but I 
# would make them a reference, since we might want to show all the reviews
# that some particular member has written. They can also grow without bound.


# Exercise 2
# Advantage: An order can be displayed without a second lookup into `products`. 
# The copy also keeps the order a faithful historical record: if the product 
# is later renamed or discontinued, old orders still show what the customer 
# actually bought.
# Disadvantage: The name is stored in many places, so it can go out of sync. 
# If a product's name is corrected, say a typo fix, every existing order keeps 
# the old name unless we update them all.


client = MongoClient("mongodb://localhost:27017/")

db = client["webshop"]


# Exercise 3
def exercise_3():
    print("--- Exercise 1 ---")
    # Start clean, so the script can be re-run. 
    # `create_collection` fails if it already exists.
    db.drop_collection("newsletter_signups")

    db.create_collection(
        "newsletter_signups",
        validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["email"],
                "properties": {
                    "email": {"bsonType": "string"},
                    "source": {"enum": ["web", "store"]},
                },
            }
        },
    )

    # Valid: email is a string, source is one of the allowed values
    result = db.newsletter_signups.insert_one(
        {"email": "alice@example.com", "source": "web"}
    )
    print("Inserted:", result.inserted_id)

    # Invalid: "phone" is not in the enum
    try:
        db.newsletter_signups.insert_one(
            {"email": "someone@example.com", "source": "phone"}
        )
        print("Inserted (this should not happen)")
    except WriteError as e:
        print("Insert rejected by validation:", e.code)


# Exercise 4
def exercise_4():
    print("--- Exercise 4 ---")
    pipeline = [
        {"$group": {"_id": "$city", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
    ]
    for row in db.customers.aggregate(pipeline):
        print(row)


# Exercise 5
def exercise_5():
    print("--- Exercise 5 ---")
    pipeline = [
        {"$group": {
            "_id": "$category",
            "cheapest": {"$min": "$price"},
            "most_expensive": {"$max": "$price"},
        }},
    ]
    for row in db.products.aggregate(pipeline):
        print(row)


# Exercise 6
def exercise_6():
    print("--- Exercise 6 ---")
    pipeline = [
        {"$group": {"_id": "$customer_id", "orders": {"$sum": 1}}},
        {"$match": {"orders": {"$gte": 2}}},
    ]
    for row in db.orders.aggregate(pipeline):
        print(row)


# Exercise 7
def exercise_7():
    print("--- Exercise 7 ---")
    pipeline = [
        {"$project": {"n_items": {"$size": "$items"}}},
    ]
    for row in db.orders.aggregate(pipeline):
        print(row)


# Exercise 8
def exercise_8():
    print("--- Exercise 8 ---")
    pipeline = [
        {"$match": {"status": {"$ne": "cancelled"}}},
        {"$unwind": "$items"},
        {"$lookup": {
            "from": "products",
            "localField": "items.product_id",
            "foreignField": "_id",
            "as": "product",
        }},
        {"$unwind": "$product"},
        {"$group": {
            "_id": "$product.category",
            "units_sold": {"$sum": "$items.quantity"},
        }},
    ]
    for row in db.orders.aggregate(pipeline):
        print(row)


# Exercise 9
def exercise_9():
    print("--- Exercise 9 ---")
    pipeline = [
        {"$unwind": "$items"},
        {"$group": {
            "_id": "$status",
            "revenue": {"$sum": {"$multiply": ["$items.quantity", "$items.unit_price"]}},
        }},
    ]
    for row in db.orders.aggregate(pipeline):
        print(row)


# Exercise 10
def exercise_10():
    print("--- Exercise 10 ---")
    pipeline = [
        {"$unwind": "$tags"},
        {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
    ]
    for row in db.products.aggregate(pipeline):
        print(row)


# Exercise 11
def exercise_11():
    print("--- Exercise 11 ---")

    def find_orders_unsafe(request_text):
        data = json.loads(request_text)
        return list(db.orders.find({"status": data["status"]}))

    def find_orders(request_text):
        data = json.loads(request_text)
        status = data.get("status")
        if not isinstance(status, str):
            return []
        return list(db.orders.find({"status": status}))

    normal = '{"status": "new"}'
    attack = '{"status": {"$ne": "x"}}'

    print("Unsafe:", len(find_orders_unsafe(normal)), len(find_orders_unsafe(attack)))
    print("Safe:  ", len(find_orders(normal)), len(find_orders(attack)))


# Exercise 12
def exercise_12():
    print("--- Exercise 12 ---")

    def products_under(text):
        try:
            limit = float(text)
        except ValueError:
            print("Please enter a number.")
            return []
        return list(db.products.find(
            {"price": {"$lt": limit}},
            {"name": 1, "price": 1, "_id": 0},
        ))

    for text in ["300", "abc", '{"$gt": 0}']:
        print(text, "->", products_under(text))


# Running exercises
if __name__ == "__main__":
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    # exercise_7()
    # exercise_8()
    # exercise_9()
    # exercise_10()
    exercise_11()
    exercise_12()
