
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
        status = e.response.status_code
        message = f"Error: server answered {status} ({url})"
        try:
            body = e.response.json()
            if isinstance(body, dict) and body.get("message"):
                message += f": {body['message']}"
        except ValueError:
            pass  # the error body was not JSON, keep the short message
        print(message)
    except requests.exceptions.JSONDecodeError:
        print("Error: the answer was not valid JSON")
    except requests.exceptions.RequestException as e:
        print(f"Error: request failed: ({type(e).__name__}) {e}")
    return None
