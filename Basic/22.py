'''
23. String Prefix Copies

Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
'''

def prefix_copies(string, copies):
    if len(string) < 2:
        return string * copies
    else:
        return string[:2] * copies

print(prefix_copies("Hello", 2))
print(prefix_copies("A", 3))
print(prefix_copies("", 5))