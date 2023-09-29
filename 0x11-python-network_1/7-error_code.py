#!/usr/bin/python3
"""
A script that accepts a URL, requests the URL,
and then displays the content of the answer decoded in utf-8.
Print the following if the HTTP status code is greater than or equal to 400:
Error code, followed by the HTTP status code's value.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    body = response.text
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(body)
