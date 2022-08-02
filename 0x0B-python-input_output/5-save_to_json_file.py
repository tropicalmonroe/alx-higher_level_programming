#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an obj to tx json rep"""
    with open(filename, "w") as x:
        json.dump(my_obj, x)
