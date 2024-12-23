'''
4. Circle Area Calculator

Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''

from math import pi
print("Program to find area of a circle")
radius = float(input("Enter the value of radius: "))

# calculate area of circle 
area = pi*(radius**2)

print(f"The are of circle with radius {radius} is {area}")