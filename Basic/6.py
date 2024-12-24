'''
6. List and Tuple Generator

Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

num_input = input("Enter sequence of numbers like 1,2,3,4:")

# generate list
list_u = num_input.split(",")
print("The generated list is:", list_u)

# generate tuple
tuple_u = tuple(num_input.split(","))
print("The generated tuple is:", tuple_u)