# Change List Items

fruits = ['Apple', 'Banana', 'Cherry', 'Papaya', 'Guava']

# fruits[5] = "Banana"
# IndexError: list assignment index out of range

fruits [4] = "Mango"
print(fruits)
# ['Apple', 'Banana', 'Cherry', 'Papaya', 'Mango']

# 2. Update Range

fruits[0:2] = ["Pomegranate", "Muskmelon"]
print(fruits)

fruits[3:6] = ["Watermelon", "Kafal"]
print(fruits)

# 3. Insert Items
# append() and insert() method
# append() method adds element to the end of the list

# insert method adds elements to a particular/given index in the list

# 3.1 append() method

fruits.append("Hisalu")
print(fruits)

# 3.2 insert() method
# insert item without replacing any existing value

# list_name.insert(index, elements)
fruits.insert(0, "Jamun")
print(fruits)
