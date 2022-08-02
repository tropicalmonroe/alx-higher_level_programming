#!/usr/bin/python3
"""Defines a str JSON function."""
import json


def to_json_string(my_str):
    """Return representation of str JSON"""
    return json.loads(my_str)
