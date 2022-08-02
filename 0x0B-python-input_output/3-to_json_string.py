#!/usr/bin/python3
"""defines JSON func"""
import json


def to_json_string(my_obj):
    """Return JSON rep of str obj"""
    return json.dumps(my_obj)
