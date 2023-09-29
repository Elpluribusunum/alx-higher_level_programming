#!/usr/bin/python3
"""
X-Request-Id value is displayed in the header of the response by a Python
script that accepts a URL, makes a request to the URL, and displays
the value of the variable.
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        value = html.get('X-Request-Id')
        print(value)
