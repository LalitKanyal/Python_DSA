#1.2.1 IDENTIFIERS, OBJECTS, AND THE ASSIGNMENT STATEMENT

# Python is OOP. Python's built in classes - int, float , str

temperature = 98.6
print("Real Temperature:", temperature)

# original identifier taking reference
original = temperature
print("original temperature:", original)

# temperature identifier has been assigned to a new value
temperature = temperature + 5.0
print("Updated Temperature: ", temperature)

# but "original" identifier continues to refer to the previously existing value
print("Original temperature after update: ", original)

