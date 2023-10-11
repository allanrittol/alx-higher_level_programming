#!/usr/bin/python3
def uppercase(str):
    # Define a dictionary to map lowercase letters to uppercase
    result = ''
    for char in str:
        if 'a' <= char <= 'z':
            print(char(ord(char)) - 32), end='')
        else:
            print(char, end='')
    print('\n')
    uppercase("hello world")
