#!/usr/bin/python3
"""defines a function for looking up object attributes."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
