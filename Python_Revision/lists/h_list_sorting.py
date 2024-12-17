# List sorting

# 1. sort alphanumerically

fruits = ['Muskmelon', 'Pomegranate', 'Cherry', 'Watermelon', 'Kafal', 'Hisalu']
fruits.sort()
print(fruits)
# ['Cherry', 'Hisalu', 'Kafal', 'Muskmelon', 'Pomegranate', 'Watermelon']

nums = [2, 4, 234, -23, 33.0, 0.00, 0, -0]
nums.sort()
print(nums)
# [-23, 0.0, 0, 0, 2, 4, 33.0, 234]

# 2. Sort Descending

fruits.sort(reverse=True)
print(fruits)

# 3. check if sort() updates the list completely
new_flist = fruits.append('Kiwi')
print(new_flist)
# returns None 
'''
The append() method adds an item to the end of the list in place 
and does not return a new list. Instead, it modifies the
original list 
and returns None.
'''
print(fruits)
# ['Watermelon', 'Pomegranate', 'Muskmelon', 'Kafal', 'Hisalu', 'Cherry', 'Kiwi']

# 4. Case Insensitive Sort
# all capital letters are sorted before lower case

fruits_il = ["apple", "Banana", "cherry", "Pomegranate"]
fruits_il.sort()
print(fruits_il)
# ['Banana', 'Pomegranate', 'apple', 'cherry']

# solution is using key = function
# we can customize our function here

fruits_il.sort(key= str.lower)
print(fruits_il)
# ['apple', 'Banana', 'cherry', 'Pomegranate']

# 5. reverse the list

# fruits_il = ['apple', 'Banana', 'cherry', 'Pomegranate']
fruits_il.reverse()
print(fruits_il)
# ['Pomegranate', 'cherry', 'Banana', 'apple']
