# Boolean Practice

print(True and True)
# True

print(False and True)
# False

print(1 == 1 and 2 == 1)
# False

print("test" == "test")
# True

print(1 == 1 or 2 != 1)
# True

print(True and 1 == 1)
# True

print(False and 0 != 0)
# False

print(True or 1 == 1)
# True

print("test" == "testing")
# False

print(1 != 0 and 2 == 1)
# False

print("test" != "testing")
# True

print("test" == 1)
# False

print(not(True and False))
# True

print(not (1 == 1 and 0 != 1))
# False

print (not (10 == 1 or 1000 == 1000))
# False

print(not (1 != 10 or 3 == 4))
# False

print(not ("testing" == "testing" and "Zed" == "Cool Guy"))
# True

print(1 == 1 and (not ("testing" == 1 or 1 == 0)))
# True

print("chunky" == "bacon" and (not (3 == 4 or 3 ==3)))
# False

print(3 != 3 and (not ("testing" == "testing" or "Python" == "Fun")))
# False

print("python" == "Python")
# False

print("test" and "test")
# test

print(1 and 1)
# 1

print(0 and 1)
# 0

print(1 and 2)
# 2

print(2 and 4)
# 4

'''
Rules of and in Python
If the first operand is falsy, and returns the first operand.
If the first operand is truthy, and returns the second operand.
'''
# Case 1: First operand is falsy
print(0 and 5)
# 0

# Case 2: First operand is truthy
print(3 and 5)
# 5

# Case 3: First operand is falsy, regardless of second operand
print(None and "Hello")
# None

# print(1 <> 2)
# <> is deprecated, use !=


'''

! Tip: 

Any and expression that has a False is immediately False.
Any or expression that has a True is immediately True.

'''
