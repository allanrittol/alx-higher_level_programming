#!/usr/bin/python3
"""Defining save_to_json_file function"""


import json


def save_to_join_file(my_obj, filename):
    """writes an object to text file"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
