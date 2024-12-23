'''
5. Reverse Full Name

Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
'''

# Input first and last name
f_name = input("Enter your First Name:")
l_name = input("Enter your last name:")

name_in_order = f_name + " " + l_name
print(f"Name in order: {name_in_order}")
print(name_in_order)

name_in_reverse = l_name + " " + f_name
print(f"Name in reverse order: {name_in_reverse}")