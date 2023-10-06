#!/usr/bin/python3
def uppercase(str):
    # Define a dictionary to map lowercase letters to uppercase
    result = ''
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("Original String: {}".format(str))
    print("Uppercase String: {}".format(result))
