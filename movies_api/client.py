
import os
from dotenv import load_dotenv
from pprint import pprint
import requests
from api_client import get_json


BASE_URL = "http://127.0.0.1:8000"

load_dotenv()
key = os.getenv("API_KEY")

pprint(get_json(f"{BASE_URL}/movies"), sort_dicts=False)
get_json(f"{BASE_URL}/movies/99")

new_movie = {"title": "Underground", "director": "Emir Kusturica", "year": 1995}
with_key = requests.post(f"{BASE_URL}/movies", json=new_movie,
                         headers={"X-API-Key": key}, timeout=5)
without_key = requests.post(f"{BASE_URL}/movies", json=new_movie, timeout=5)
print(with_key.status_code, with_key.json())    # 201 + new movie
print(without_key.status_code)                  # 401
