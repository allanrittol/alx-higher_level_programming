#!/usr/bin/python3
"""Defining save_to_json_file function"""


import json


def save_to_join_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Parameters:
        my_obj: The object to be serialized and saved to the file.
        filename (str): The name of the file to save the JSON representation.

    Note:
        This function uses the 'with' statement to ensure proper file handling.
        No exception handling is implemented for object serialization or
        file permissions.

    Example:
        save_to_json_file({"name": "John", "age": 30}, "output.json")
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
