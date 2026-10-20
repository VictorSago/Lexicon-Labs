
import os
from dotenv import load_dotenv
from api_client import get_json
import requests


load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
REPOS_URL = "https://api.github.com/users/{}/repos"


# Task 3
def get_gh_info():
    print("--- Task 3 ---")
    if not TOKEN:
        print("GITHUB_TOKEN not found. Check your .env file.")
        return

    username = input("GitHub username: ").strip()
    repos = get_json(
        REPOS_URL.format(username),
        params={"sort": "pushed", "per_page": 5},
        headers={"Authorization": f"Bearer {TOKEN}"},
    )
    if repos is None:
        print(f"Could not get repositories for '{username}'.")
        return
    if not repos:
        print(f"'{username}' has no public repositories.")
        return
    for repo in repos:
        print(repo["name"])


# Task 4
def proof_of_use():
    print("--- Task 4 ---")
    if not TOKEN:
        print("GITHUB_TOKEN not found. Check your .env file.")
        return

    url = REPOS_URL.format("torvalds")
    params = {"sort": "pushed", "per_page": 5}
    try:
        with_token = requests.get(
            url, params=params, timeout=5,
            headers={"Authorization": f"Bearer {TOKEN}"},
        )
        without_token = requests.get(url, params=params, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return

    print("With token:   ", with_token.headers.get("X-RateLimit-Limit"))
    print("Without token:", without_token.headers.get("X-RateLimit-Limit"))


# Task 5
# The following code corrupts the token in memory, and then tries to access 
# GitHub with the corrupted token
def corrupt_token_access():
    print("--- Task 5 ---")
    if not TOKEN:
        print("GITHUB_TOKEN not found. Check your .env file.")
        return

    bad_token = TOKEN[:-1] + ("x" if TOKEN[-1] != "x" else "y")
    get_json(
        REPOS_URL.format("torvalds"),
        params={"sort": "pushed", "per_page": 5},
        headers={"Authorization": f"Bearer {bad_token}"},
    )
# 401 vs 403:
# 401 Unauthorized means authentication failed: the server does not know
# who you are, because the credentials are missing, wrong or expired.
# 403 Forbidden means authorization failed: the server knows who you are,
# but you are not allowed to do this (for example a missing scope, or a
# rate limit that is used up). Sending the same request again with
# different credentials can fix a 401, but never a 403 for the same user.


if __name__ == "__main__":
    get_gh_info()
    proof_of_use()
    corrupt_token_access()
