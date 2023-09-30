#!/usr/bin/python3
"""
a script that takes two inputs and lists 10 commits made by the
user "rails" to the repository rails in chronological order from most recent
Print each line of every commit with the phrase sha>: author name>
The repository name will be the first argument.
The owner name will be the second parameter.
"""
import sys
import requests


if __name__ == "__main__":
    try:
        repo_name = sys.argv[1]
        username = sys.argv[2]
        commmits_url = "https://api.github.com/repos/{}/{}/commits" \
            .format(username, repo_name)
        response = requests.get(commmits_url)
        json_obj = response.json()
        for i, obj in enumerate(json_obj):
            if i == 10:
                break
            if type(obj) is dict:
                name = obj.get('commit').get('author').get('name')
                print("{}: {}".format(obj.get('sha'), name))
    except ValueError as invalid_json:
        pass
