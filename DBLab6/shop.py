
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
    try:                                                    # Exercice 7
        price = float(input("Price: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Price must be a number and stock a whole number. Nothing saved.")
        return
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")


# Exercise 5
def change_stock(conn):
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


# Exercise 6
def show_receipt(conn):
    try:
        order_id = int(input("Order id: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    cursor = conn.execute(
        """SELECT p.name, oi.quantity, oi.unit_price,
                  oi.quantity * oi.unit_price AS line_total
           FROM order_items oi
           JOIN products p ON p.product_id = oi.product_id
           WHERE oi.order_id = ?""",
           (order_id,)
           )
    rows = cursor.fetchall()
    if not rows:
        print("No order with that id.")
        return
    total = 0
    for name, quantity, unit_price, line_total in rows:
        print(f"{name:<20} {quantity:>3} x {unit_price:>8.2f} = {line_total:>9.2f} kr")
        total += line_total
    print(f"{'Total':<20} {'':>16}   {total:>9.2f} kr")


def main():
    conn = get_connection()          # was: `conn = connect()`
    while True:
        print("\n1) List products  2) Search customers  3) Add product"
              "\n4) Change stock  5) Receipt  0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            show_receipt(conn)
        elif choice == "0":
            break
    conn.close()


main()
