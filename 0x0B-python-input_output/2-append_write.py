#!/usr/bin/python3
"""Defiition of append_write function"""


def append_write(filename="", text=""):
    """appends filename wuth UTF-8"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
