
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


# Exercise 9
def exercise_9():
    print("--- Exercise 9 ---")
    with connect() as conn:
        cursor = conn.execute(
            """SELECT DISTINCT p.name
               FROM orders o
               JOIN order_items oi ON oi.order_id = o.order_id
               JOIN products p ON p.product_id = oi.product_id
               WHERE o.customer_id = 1""")
        for (name,) in cursor.fetchall():
            print(name)


# Exercise 10
def exercise_10():
    print("--- Exercise 10 ---")
    with connect() as conn:
        cursor = conn.execute(
            "UPDATE customers SET email = ? WHERE first_name = ? AND last_name = ?", 
            ("erik.johansson@example.com", "Erik", "Johansson")
        )
        print(f"{cursor.rowcount} row changed")
        conn.rollback()  # like Revert Changes: webshop.db stays unchanged


# Exercise 11
def exercise_11():
    print("--- Exercise 11 ---")
    with connect() as conn:
        conn.execute("BEGIN")
        conn.execute(
            """CREATE VIEW customer_overview AS 
            SELECT c.customer_id, c.first_name, c.city, 
                    COUNT(o.order_id) AS number_of_orders
            FROM customers c
            LEFT JOIN orders o ON o.customer_id = c.customer_id
            GROUP BY c.customer_id"""
        )
        for row in conn.execute("SELECT * FROM customer_overview"):
            print(row)
        conn.rollback()  # like Revert Changes: the view is not kept


# Exercise 12
# “Just in case” isn’t a good reason to collect personal data. Under GDPR we 
# should only store what we need for a clear purpose, and a birth date we never 
# use is a privacy risk if the data leaks, so we should add it only when a real 
# need appears, such as selling age-restricted products.


# Running exercises
if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_9()
    exercise_10()
    exercise_11()
