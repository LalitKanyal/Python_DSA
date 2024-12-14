#mutable and immutable classes

# A class is immutable if each object of that class has a fixed value upon instantiation that cannot subsequently be changed

""" Class           description                         immutable?

    bool            Boolean value                       yes
    int             integer                             yes
    float           floating point num                  yes
    list            mutable sequence of objects         no
    tuple           immutable sequence of objects       yes
    str             character string                    yes
    set             unordered set of distinct objects   no
    frozenset       immutable form of set class         yes
    dict            associative mapping (dictionary)    no
"""

# 1. Bool Class
#The bool class is used to manipulate logical (Boolean) values, and the only two instances of that class are expressed as the literals True and False.
print(bool(0))
print(bool(1))

# 2. Int Class
# The int class is designed to represent integer values 

print(1)
print(-12)
print(0x7f)
print(int(0x7f))
print(hex(12))
print(oct(127))
print(0o127)

#The integer constructor, int(), returns value 0 by default.
print(int());

f = 1.9923
print(f)
# 1.9923
print(int(f))
# 1
print(float(f))
# 1.9923

print(int('123'))
# 123
# print(int('hello'))
# ValueError

# conversion from different base
print(int('7f', 16))
# 127


# 3. The float Class

# The float class is the sole floating-point type in Python

print(2.0)
print(2.)
print(float(2))
# 2.0

print(6.022e23)
# 6.022e+23
print(float('3.14'))
# 3.14

# Sequence Types: The list, tuple, and str Classes
'''
    a. order is significant
    b. list is same like array in other languages
    c. tuple class is an immutable version of list
    d. str class is to represent immutable sequence of text characters

'''

# 4. List Class
'''
A list instance stores a sequence of objects. 
lists are array based sequence and are zero indexed
[]
list() constructor
'''
colors = ['red', 'green', 'blue']
print(colors)

#list() constructor
name_list = list('Lalit')
print(name_list)

# 5. Tuple Class
'''
tuple class provides an immutable version of a sequence
( )
'''

number1 = (17, 18)
print(type(number1))
# <class 'tuple'>  because it contains multiple elements separated by a comma.

a = 17, 18
print(type(a))
# <class 'tuple'>

b = 17, 
print(type(b))
# <class 'tuple'>
# this is a one-element tuple

number = (17)
print(type(number))
# returns <class 'int'>  because the parentheses are treated as grouping parentheses
# without the trailing comma, the expression (17) is viewed as a simple parenthesized numeric expression.


'''
6. str Class

a. str class is specifically designed to efficiently represent an immutable sequence of characters
b. string literals can be closed in single like 'hello' or double quotes like "hello"
c. Escape character
d. Delimiter to begin and end a string literal
'''

# escape character
print('I can\'t sleep')
print("I can't sleep")
print('C:\\Python\\')

# delimiter
print("""
Hey
    this is
example of delimiter.
    Do you see the 
space here.
""")

'''
7. set and frozenset classes

a. Set items are unordered and without duplicates
b. advantage of set over list is they are optimized to look for a specific element contained in the set.
c. set is based on DS hash table.
d. unordered and immuntable instances like integers, floating-point num and character strings can be elements of a set.
e. The frozenset class is an immutable form of the set type, so it is legal to have a set of frozensets.
f. curly braces as delimiters for a set. ex - {18}
g. The exception to this rule is that { } does not represent an empty set; for historical reasons, it represents an empty dictionary
'''

set1 = {'red', 'green', 'blue'}
print(set1)

# represents empty dictionary
print(type({}))

# create empty set
print(set())

print(set('Hello'))
# {'e', 'o', 'l', 'H'}
# because duplicate l is ignored and sets are unordered

print(len(set('hello')))
# 4

'''
8. dict Class

8a. Python's dict class represents a dictionary, or mapping, from a set of distinct keys to associated values.
8b. A nonempty dictionary is expressed using a comma-separated series of key:value pairs.
'''

country = {'in': 'India', 'de': 'Germany', 'ir': 'Iran', 'ru': 'Russia'}
print(country)