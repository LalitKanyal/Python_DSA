# List challenge

fruit = [
    ['Apples', 12, 'AAA'],
    ['Oranges', 1, 'B'],
    ['Pears', 2, 'A'],
    ['Grapes', 14, 'UR']
]

# Fruit Challenge
# elements out of the fruit variable

# 12
print(fruit[0][1])

# 'AAA'
print(fruit[0][2])

# '2'
print(fruit[2][1])

# 'Oranges'
print(fruit[1][0])

# 'Grapes'
print(fruit[3][0])

# 14
print(fruit[3][1])

# 'Apples'
print(fruit[0][0])

# Cars Challenge
# get elements out of the cars variable

cars = [
    ['Tata', ['Black', 'Big', 34500]],
    ['Mahindra', ['Red', 'Little', 1000000]],
    ['Suzuki', ['Blue', 'Medium', 1234]],
    ['BMW', ['White', 'Baby', 7890]]
]

# 'Big'
print(cars[0][1][1])

#'Red'
print(cars[1][1][0])

#1234
print(cars[2][1][2])

#'White'
print(cars[3][1][0])

#7890
print(cars[3][1][2])

#'Black'
print(cars[0][1][0])

#34500
print(cars[0][1][2])

#'Blue'
print(cars[2][1][0])


# Language Challenge
# get elements out of the languages variable

languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['JavaScript', ['Moderate', ['Alright', 'Bizarre']]],
    ['Perl6', ['Moderate', ['Fun', 'Weird']]],
    ['C', ['Fast', ['Annoying', 'Dangerous']]],
    ['Forth', ['Fast', ['Fun', 'Difficult']]],
]

# 'Slow'
print(languages[0][1][0])

# 'Alright'
print(languages[1][1][1][0])

# 'Dangerous'
print(languages[3][1][1][1])

# 'Fast'
print(languages[3][1][0])
print(languages[4][1][0])

# 'Difficult'
print(languages[4][1][1][1])

# 'Fun'
print(languages[2][1][1][0])

# 'Annoying'
print(languages[3][1][1][0])

# 'Weird'
print(languages[2][1][1][1])

# 'Moderate'
print(languages[1][1][0])
print(languages[2][1][0])



# FINAL CHALLENGE

# Figure out what these will return without running, just watch the list and figure
print(cars[1][1][1])
print(cars[1][1][0])
print(cars[1][0])
print(cars[3][1][1])
print(fruit[3][2])
print(languages[0][1][1][1])
print(fruit[2][1])
print(languages[3][1][0])
