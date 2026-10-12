
#import sqlite3
from db import get_connection

# Improved and moved to `db.py`
# def connect():
#     conn = sqlite3.connect("webshop.db")
#     conn.execute("PRAGMA foreign_keys = ON")
#     return conn


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")


def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)


def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")


# Exercise 5
def change_stock(conn):                                   # Exercise 5
    try:
        product_id = int(input("Product id: "))
        new_stock = int(input("New stock: "))
    except ValueError:
        print("Please enter whole numbers. Nothing changed.")
        return
    cursor = conn.execute("UPDATE products SET stock = ? WHERE product_id = ?", (new_stock, product_id))
    conn.commit()
    if cursor.rowcount == 0:
        print("No product with that id.")
    else:
        print("Stock updated!")


def main():
    conn = get_connection()          # was: `conn = connect()`
    while True:
        print("\n1) List products  2) Search customers  3) Add product"
              "\n4) Change stock  0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "0":
            break
    conn.close()


main()
