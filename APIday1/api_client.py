
import requests


def get_json(url, params=None, headers=None, timeout=5):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print(f"Error: the request timed out ({url})")
    except requests.exceptions.ConnectionError:
        print(f"Error: could not connect to the server ({url})")
    except requests.exceptions.HTTPError as e:
        print(f"Error: server answered {e.response.status_code} ({url})")
    except requests.exceptions.JSONDecodeError:
        print("Error: the answer was not valid JSON")
    except requests.exceptions.RequestException as e:
        print(f"Error: request failed: ({type(e).__name__}) {e}")
    return None
