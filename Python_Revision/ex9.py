# Inputs

'''
end paramenter

print() function by default adds a newline at the end of the output, 
 we can control it using end parameter
'''
print("What is your name?", end=' ')
#print("What is your name? ")
name = input()
print(f"Your name is {name}")


# Other way to take input by directly setting input to variable

age = int(input("What is your age? "))
print(f"You are {age} years old")

# error handling in the code> if user enter string as age

try:
    age1 = int(input("What is your age? "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a integer for your age.")

