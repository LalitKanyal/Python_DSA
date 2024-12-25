'''
Triple Sum Calculator

Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
'''

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

if a == b == c:
    sum = (a + b + c) * 3
    print(sum)
else:
    sum = a + b + c
    print(sum)