#!/usr/bin/python3
# 6-from_json_string.py
"""This defines the JSON to Object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
