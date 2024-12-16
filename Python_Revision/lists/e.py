# Remove item

fruits = ['Pomegranate', 'Muskmelon', 'Cherry', 'Watermelon', 'Kafal', 'Hisalu']

fruits.remove("Pomegranate")
print(fruits)

# remove the first occurence of item to be removed

fruits = ['Pomegranate', 'Muskmelon', 'Pomegranate','Cherry', 'Watermelon', 'Kafal', 'Hisalu']
fruits.remove("Pomegranate")
print(fruits)

# returns 
# ['Muskmelon', 'Pomegranate', 'Cherry', 'Watermelon', 'Kafal', 'Hisalu']

# 2.  pop() method remove specific index using pop() method

fruits.pop(0)
print(fruits)

# if no index, last item will be removed
fruits.pop()
print(fruits)

# 3. delete keyword

del fruits[0]
print(fruits)
# ['Cherry', 'Watermelon', 'Kafal']

# 4. clear() method
fruits.clear()
print(fruits)
# returns []
print(fruits)