
import os
from dotenv import load_dotenv
from api_client import get_json


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


if __name__ == "__main__":
    get_gh_info()
