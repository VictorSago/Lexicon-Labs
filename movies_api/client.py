
from api_client import get_json
from pprint import pprint
import requests


BASE = "http://127.0.0.1:8000"

pprint(get_json(f"{BASE}/movies"), sort_dicts=False)
get_json(f"{BASE}/movies/99")

new_movie = {"title": "Underground", "director": "Emir Kusturica", "year": 1995}
response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5)
print(response.status_code, response.json())
