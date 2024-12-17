# Python - List Comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "o" in the name.

# 1. normal way using for loop

fruits = ['muskmelon', 'pomegranate', 'Cherry', 'Watermelon', 'Kafal', 'Hisalu']
new_list = []

for x in fruits:
    if "o" in x:
        new_list.append(x)
print(new_list)

# 2. using list comprehension
vegetables = ["Potato", "Tomato", "Okra", "Bottle gourd", "Pumpkin", "Spinach"]

new_list_vege = [x for x in vegetables if "o" in x]

# new_list_vege = [expression/variable for x in iterable/here existing list if condition == True]

print(new_list_vege)
# ['Potato', 'Tomato', 'Bottle gourd']

# 3. original list will be unchanged
print(vegetables)
# ['Potato', 'Tomato', 'Okra', 'Bottle gourd', 'Pumpkin', 'Spinach']


# 4. condition is like filter
condition_comprehension = [x for x in vegetables if x != "Okra"]
print(condition_comprehension)
# returns ['Potato', 'Tomato', 'Bottle gourd', 'Pumpkin', 'Spinach']

# 5. without if condition (condition is optional)
removed_if = [x for x in vegetables]
print(removed_if)
# prints all list items
# ['Potato', 'Tomato', 'Okra', 'Bottle gourd', 'Pumpkin', 'Spinach']

# 6. Iterable
# range() function to create an iterable

new_list_iteable = [x for x in range(11)]
print(new_list_iteable)

new_list_iteable_if = [x for x in range(11) if x <6]
print(new_list_iteable_if)

# 7. Expression
# It's the current item in the iteration, we can manipulate it

# capitalize method capitalizes the first character of string
# fruits = ['muskmelon', 'pomegranate', 'Cherry', 'Watermelon', 'Kafal', 'Hisalu']
expression_list = [x.capitalize() for x in fruits ]
print(expression_list)
# ['Muskmelon', 'Pomegranate', 'Cherry', 'Watermelon', 'Kafal', 'Hisalu']
expression_list = [x.upper() for x in fruits ]
print(expression_list)
# ['MUSKMELON', 'POMEGRANATE', 'CHERRY', 'WATERMELON', 'KAFAL', 'HISALU']



