#!/usr/bin/python3
"""
X-Request-Id value is displayed in the header of the response by a Python
script that accepts a URL, makes a request to the URL
and displays the value of the variable.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    value = response.headers.get("X-Request-Id")
    print(value)
