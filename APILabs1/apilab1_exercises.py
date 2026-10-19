
import requests
from api_client import get_json


BASE = "https://fakestoreapi.com"


# Exercise 1
def exercise_1():
    print("--- Exercise 1 ---")
    products = get_json(f"{BASE}/products")
    if products is None:
        return
    for p in sorted(products, key=lambda p: p["price"]):
        print(f"{p['price']:>8.2f}  {p['title']}")


# Exercise 2
def exercise_2():
    print("--- Exercise 2 ---")
    categories = get_json(f"{BASE}/products/categories")
    if categories is None:
        return
    print(categories)

    name = input("Category: ").strip()
    products = get_json(f"{BASE}/products/category/{name}")
    # An unknown category gives an empty list, not an error
    if not products:
        print(f"No products found for category '{name}'.")
        return
    cheapest = min(products, key=lambda p: p["price"])
    print(f"{len(products)} products, cheapest: {cheapest['title']} (${cheapest['price']})")


# Exercise 4
def exercise_4():
    print("--- Exercise 4 ---")
    new_product = {
        "title": "Test product",
        "price": 12.5,
        "description": "Just a test",
        "image": "https://i.pravatar.cc",
        "category": "electronics",
    }
    try:
        r = requests.post(f"{BASE}/products", json=new_product, timeout=5)
        r.raise_for_status()
        print("POST:", r.status_code, r.json())

        r = requests.patch(f"{BASE}/products/7", json={"price": 19.99}, timeout=5)
        r.raise_for_status()
        print("PATCH", r.status_code, r.json())
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


# Exercise 5
def exercise_5():
    print("--- Exercise 5 ---")
    cases = [
        ("Wrong URL", f"{BASE}/does-not-exist", 5),
        ("Timeout", f"{BASE}/products", 0.001),
        ("Made-up domain", "https://this-domain-does-not-exist-12345.com", 5),
    ]
    for label, url, timeout in cases:
        print(f"{label}:")
        result = get_json(url, timeout=timeout)
        if result is None:
            print("  -> handled, program continues")


# Running exercises
if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_4()
    exercise_5()
