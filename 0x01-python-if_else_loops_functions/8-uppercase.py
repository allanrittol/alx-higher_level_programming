#!/usr/bin/python3
def uppercase(str):
    # Define a dictionary to map lowercase letters to uppercase
    for char in str:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:  # ASCII values for lowercase letters
            ascii_val -= 32  # Convert to uppercase
        print("{:c}".format(ascii_val), end='')
        print("")
