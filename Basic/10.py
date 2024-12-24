'''
10. Number Expansion Calculator

Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''

n = input("Enter an integer:")
print("n", n)
sum = int(n) + int(n*2) + int(n*3)

# note that n+nn+nnn here we are concatenating the digit n
# nn means concatenating the digit n twice as a string
# if n is 5 then nn means 55

print("The value of entered integer for formula n+nn+nnn is:", {sum})