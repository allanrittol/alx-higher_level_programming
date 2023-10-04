#!/usr/bin/python3
def uppercase(str):
    # Define a dictionary to map lowercase letters to uppercase
    upper_map = {chr(i): chr(i - 32) for i in range(97, 123)}
    
    # Initialize an empty string for the result
    result = ""
    
    # Iterate over the input string
    for char in str:
        # If the character is a lowercase letter, convert it to uppercase
        if 'a' <= char <= 'z':
            result += upper_map[char]
        else:
            result += char
    
    # Print the result
    print(result)
    print()

