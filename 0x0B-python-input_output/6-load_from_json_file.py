#!/usr/bin/python3
"""a function that creates an Object frm jsonfile"""
import json


def load_from_json_file(filename):
    """creating python obj from a json file"""
    with open(filename) as x:
        return json.load(x)
