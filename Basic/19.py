'''
String Copy Generator

Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
'''

def str_copy(times, string):
    if times < 0:
        return "Error: 'times' must be a non-negative integer."
    result = times * string
    return result

print(str_copy(3, "Hello"))

