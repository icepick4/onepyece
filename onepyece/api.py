"""
This module contains the functions to get data from the API
"""
import requests


def get_data(url):
    """
    Get data from the API

    See https://api-onepiece.com/documentation for more information

    :param url: The url to get the data from
    :return: The data from the API or None if no data is found
    """
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return None if response.json() is None or response.json() == [] else response.json()
