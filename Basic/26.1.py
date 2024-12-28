'''
27. List to String Concatenator

Write a Python program that concatenates all elements in a list into a string and returns it.
'''

def string_concatenator(str_value):

    result = ""

    for i in str_value:
        result += str(i)
    return result

print(string_concatenator([1,2,"3","Hello"]))