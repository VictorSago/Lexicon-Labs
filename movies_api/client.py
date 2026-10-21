
from api_client import get_json
from pprint import pprint
import requests


BASE_URL = "http://127.0.0.1:8000"

pprint(get_json(f"{BASE_URL}/movies"), sort_dicts=False)
get_json(f"{BASE_URL}/movies/99")

new_movie = {"title": "Underground", "director": "Emir Kusturica", "year": 1995}
response = requests.post(f"{BASE_URL}/movies", json=new_movie, timeout=5)
print(response.status_code, response.json())
