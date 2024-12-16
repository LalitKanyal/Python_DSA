fruits = ["Apple", "Banana", "Cherry"]
print(fruits)


#List Items
# Ordered, changeable, allow duplicate values

# Allow Duplicates
fruits_0 = ["Apple", "Banana", "Cherry", "Papaya", "Apple"]
print(fruits_0)

# test
fruits_1 = [fruits, "Apple"]
print(fruits_1)

# length of list

# !!!!!!!!!!!!!!!!!!!!!!!!!!
# print(fruits_0.len())
'''
We can't use directly len() function in list object

AttributeError: 'list' object has no attribute 'len'
'''

print(len(fruits_1))
# 2

# Data types of list items

# can be of any type

list_items_type = ["apple", 2, 34.34, None, not(0), 0 and 1, 0 or 1]
print(list_items_type)

# ['apple', 2, 34.34, None, True, 0, 1]


# list() constructor
# to create a new list

# directly creating list
dir_list = ["Yo", "Direct", "List"]

# list constructor way to create a list

#list_constructor = list("hello", "list", "error")
#TypeError: list expected at most 1 argument, got 2

list_constructor_up = list(("Apple", 'Banana', "Cherry"))
# double round bracket
print(list_constructor_up)