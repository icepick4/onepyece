import requests

from .common import build_url


def get_data(endpoint, search=None, resource_id=None):
    url = build_url(endpoint, search, resource_id)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()