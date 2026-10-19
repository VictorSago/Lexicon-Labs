
import requests


BASE = "https://fakestoreapi.com"


def get_json(url, params=None, headers=None, timeout=5):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The request took too long")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server")
    except requests.exceptions.HTTPError as error:
        print(f"The server said no: {error.response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("The answer was not JSON")
    except requests.exceptions.RequestException as error:
        print(f"Someting else went wrong: {type(error).__name__}")
    return None


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
    print(f"{len(products)} products, cheapest: {cheapest['title']} ({cheapest['price']})")


# Running exercises
if __name__ == "__main__":
    exercise_1()
    exercise_2()
