#!/usr/bin/env python3
"""
client.py - Client-side logic for the project
"""

import requests
from typing import Any, Dict


def get_data(url: str) -> Dict[str, Any]:

    """
    Fetch data from the given URL.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        Dict[str, Any]: The data fetched from the URL.
    """
    response = requests.get(url)
    return response.json()
