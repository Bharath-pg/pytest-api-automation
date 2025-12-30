# utils/api_client.py
import requests
from config.config import BASE_URL  # import hardcoded base url

def get(endpoint, headers=None, params=None):
    default_headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    if headers:
        default_headers.update(headers)
    return requests.get(f"{BASE_URL}{endpoint}", headers=default_headers, params=params)

def post(endpoint, payload=None, headers=None):
    default_headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    if headers:
        default_headers.update(headers)
    return requests.post(f"{BASE_URL}{endpoint}", json=payload, headers=default_headers)
