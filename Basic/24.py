'''
 Value in Group Tester

Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

def is_value_in_group(value):
    group = [1, 5, 8, 3]

    return value in group

print(is_value_in_group(-1))
print(is_value_in_group(000.0))
print(is_value_in_group(1))