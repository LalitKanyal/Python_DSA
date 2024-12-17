# copy a list

# can't copy directly by assigning list to other expression like list2 = list1

# 1. using copy() method

fruits = ['apple', 'Banana', 'cherry', 'Pomegranate']
new_fruits = fruits.copy()
print(new_fruits)

fruits.clear()
print(fruits)
# original list fruits is cleared
# returns []

print(new_fruits)
# returns
# ['apple', 'Banana', 'cherry', 'Pomegranate']

# 2. make copy using list() method

vegetables = ["Potato", "Tomato", "Okra"]
new_vegetables = list(vegetables)
print(new_vegetables)
