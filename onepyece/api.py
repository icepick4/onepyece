import requests


def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return None if response.json() is None or response.json() == [] else response.json()
