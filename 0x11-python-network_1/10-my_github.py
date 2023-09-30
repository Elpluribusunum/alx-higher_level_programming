#!/usr/bin/python3
"""
script that uses the GitHub API to display your ID after receiving your
GitHub credentials username and password.
Your username will be the first argument.
Your password in your instance, a personal access token as
password will be the second argument.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    json_obj = response.json()
    print(json_obj.get("id"))
