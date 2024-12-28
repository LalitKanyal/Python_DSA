'''
Vowel Tester

Write a Python program to test whether a passed letter is a vowel or not.
'''

def vowel_tester(char):
    vowels = 'aeiou'

    return char in vowels

print(vowel_tester("b"))