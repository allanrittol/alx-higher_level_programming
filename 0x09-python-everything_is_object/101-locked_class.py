#!/usr/bin/python3
"""LockedClass definition"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attribute called 'first_name
    """
    __slots__ = ['first_name']
