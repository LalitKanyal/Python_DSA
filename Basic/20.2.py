'''
21. Even or Odd Checker

Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
'''

num = int(input("Enter a number: "))

calc = num % 2

if calc > 0:
    print("This is an odd number.")

else:
    print("This is an even number.")