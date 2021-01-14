"""
This module contains raw calls to the API
"""
import requests

from viewser.config import BASE_URL

def request(*args,path="",**kwargs):
    """
    Send a request to the API
    """
    _api_url = BASE_URL + path
    kwargs["url"] = _api_url
    return requests.request(*args,**kwargs)
