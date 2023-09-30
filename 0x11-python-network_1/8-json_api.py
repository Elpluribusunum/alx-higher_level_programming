#!/usr/bin/python3
"""
A script that accepts a letter and sends a POST request with the letter
as a parameter to http://0.0.0.0:5000/search_user.
The variable q must be used to send the letter.
Set q to "" if no argument is provided.
Display the id and name as [id>] name> if the response body is correctly
JSON structured and not empty. Otherwise: Display Invalid JSON is not a valid
JSON if both Display If the JSON is empty, no outcome.
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {"q": q}
    response = requests.post(url, data=payload)
    try:
        json_outp = response.json()
        if not json_outp:
            print("No result")
        else:
            my_id = json_outp.get("id")
            my_name = json_outp.get("name")
            print("[{}] {}".format(my_id, my_name))
    except ValueError as invalid_json:
        print("Not a valid JSON")
