'''
Triple Sum Calculator

Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
'''

def sum(a, b, c):
    add = a + b + c
    
    if a == b == c:
       add = add*3
    
    return add
        
print(sum(1,2,3))
print(sum(1,1,1))