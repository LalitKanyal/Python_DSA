'''
21. Even or Odd Checker

Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
'''

def odd_even_checker(integer):
    if integer % 2 == 0:
        return "Entered number is Even number"
    else:
        return "Entered number is Odd number"
    
print(odd_even_checker(-0))
print(odd_even_checker(298374.3))