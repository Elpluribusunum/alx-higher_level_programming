#!/usr/bin/python3
"""
a script that accepts a URL, requests the URL, and then displays
the content of the answer decoded in utf-8.
You must control urllib.error.Exceptions for HTTPError and printing:
followed by the HTTP status code and the error code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode("utf-8")
            print(response_text)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
