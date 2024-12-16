# for loop

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for num in the_count:
    print(f"This is number {num}")

for fruit in fruits:
    print(f"I love to eat: {fruit}")

for i in change:
    print(f"I see {i}")

# build list using loop
empty_list = []

# using range function

for i in range(0,11):
    print(f"Adding {i} in the list")
    empty_list.append(i)
    
for i in empty_list:
    print(f"Elements was: {i}")

'''
getting this:

[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
# create empty list
yo_list = []

for i in range(0,11):
    yo_list.append(i)
    print(yo_list)