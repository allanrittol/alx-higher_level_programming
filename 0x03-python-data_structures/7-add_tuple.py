#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If the tuple has less than 2 elements, append 0's
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # Add the first two elements of each tuple
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
