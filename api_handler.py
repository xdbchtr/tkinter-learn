import requests

def login_api(username, password):
    url = 'http://82.112.230.35:8082/login'
    payload = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to the API: {e}")
        return False

def get_products_from_api():
    url = 'http://82.112.230.35:8082/products'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"API Request failed: {e}")
        return None