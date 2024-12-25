'''
Difference from 17

Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference.
'''
a = 17.0

b = float(input("Enter a number : "))

if b <= a:
    difference = a - b
    print(f"The difference between entered number {b} and {a} is: ", difference)
else:
    difference = (b - a) * 2
    print("The difference between entered number and 17 is: ", difference )