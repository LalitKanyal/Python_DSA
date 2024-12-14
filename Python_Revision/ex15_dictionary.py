# Practice Code

# 1. Fruit Challenge

fruit = [
    {'kind': 'Apples', 'count': 12, 'rating': 'AAA'},
    {'kind': 'Oranges', 'count': 1, 'rating': 'B'},
    {'kind': 'Pears', 'count': 2, 'rating': 'A'},
    {'kind': 'Grapes', 'count': 14, 'rating': 'UR'},
    ]

# get all elements out of the fruit variable
# 12
print(fruit[0]['count'])

# 'AAA'
print(fruit[0]['rating'])

# 2
print(fruit[2]['count'])

# 'Oranges'
print(fruit[1]['kind'])

# 'Grapes'
print(fruit[3]['kind'])

# 14
print(fruit[3]['count'])

# 'Apples'
print(fruit[0]['kind'])


# 2. Cars Challenge
cars = [
    {'type': 'Cadillac', 'color': 'Black', 'size': 'Big', 'miles': 34500},
    {'type': 'Corvette', 'color': 'Red', 'size': 'Little', 'miles': 1000000},
    {'type': 'Ford', 'color': 'Blue', 'size': 'Medium', 'miles': 1234},
    {'type': 'BMW', 'color': 'White', 'size': 'Baby', 'miles': 7890}
    ]

# Big
print(cars[0]['size'])

# Red
print(cars[1]['color'])

# 1234
print(cars[2]['miles'])

# White
print(cars[3]['color'])

# 7890
print(cars[3]['miles'])

# Black
print(cars[0]['color'])

# 34500
print(cars[0]['miles'])

# Blue
print(cars[2]['color'])


# 3. Languages Challenge
languages = [
    {'name': 'Python', 'speed': 'Slow', 'opinion': ['Terrible', 'Mush']},
    {'name': 'JavaScript', 'speed': 'Moderate', 'opinion': ['Alright', 'Bizarre']},
    {'name': 'Perl6', 'speed': 'Moderate', 'opinion': ['Fun', 'Weird']},
    {'name': 'C', 'speed': 'Fast', 'opinion': ['Annoying', 'Dangerous']},
    {'name': 'Forth', 'speed': 'Fast', 'opinion': ['Fun', 'Difficult']},
    ]

# Slow
print(languages[0]['speed'])

# Alright
print(languages[1]['opinion'][0])

# Dangerous
print(languages[3]['opinion'][1])

# Fast
print(languages[3]['speed'])

# Difficult
print(languages[4]['opinion'][1])

# Fun
print(languages[2]['opinion'][0])

# Annoying
print(languages[3]['opinion'][0])

# Weird
print(languages[2]['opinion'][1])

# Moderate
print(languages[1]['speed'])
