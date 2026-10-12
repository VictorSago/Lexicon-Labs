
from db import connect


# Exercise 1
# The `connect()` function from `db.py` closes connection automatically
def exercise_1():
    with connect() as conn:
        cursor = conn.execute("SELECT first_name, last_name, city FROM customers")
        for first, last, city in cursor.fetchall():
            print(f"{first} {last} ({city})")


# Exercise 2
def exercise_2():
    max_price = float(input("Max price: "))
    with connect() as conn:
        cursor = conn.execute("SELECT name, price FROM products WHERE price < ?", (max_price,))
        for name, price in cursor.fetchall():
            print(f"{name}: {price} kr")


# Exercise 3
def exercise_3():
    category = input("Category name: ")
    with connect() as conn:
        cursor = conn.execute("SELECT COUNT(*) FROM products WHERE category = ? COLLATE NOCASE", (category,))
        count = cursor.fetchone()[0]
        print(f"There are {count} products in category {category}.")


# Exercise 4
# With an f-string, the user’s text is pasted into the SQL command itself, 
# so the input can change what the command does. For example, in Exercise 3, 
# typing x' OR '1'='1 as a category turns the filter into something that is 
# always true and returns every row. With other such input an attacker could 
# read or change data they shouldn’t touch. With a ? placeholder, the SQL and 
# the value are sent separately. The database always treats the value as plain 
# data, never as part of the command, whatever characters it contains.


# Running exercises
if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
