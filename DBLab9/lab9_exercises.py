
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


# Running exercises
if __name__ == "__main__":
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
