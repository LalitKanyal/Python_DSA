# 1. access list items

fruits_0 = ["Apple", "Banana", "Cherry", "Papaya", "Guava"]

print(fruits_0[0])
print(fruits_0[1])

# 2. negative indexing
print(fruits_0[-1])
print(fruits_0[-0])

# focus here - zero and negative zero results same

# 3. Range of indexes

print(fruits_0[1:3])
# ['Banana', 'Cherry']

print(fruits_0[0:7])
# ['Apple', 'Banana', 'Cherry', 'Papaya', 'Guava']

# list have only 5 items

print(fruits_0[:])
# ['Apple', 'Banana', 'Cherry', 'Papaya', 'Guava']

print(fruits_0[1:])
# ['Banana', 'Cherry', 'Papaya', 'Guava']

print(fruits_0[3:5])
# ['Papaya', 'Guava']

print(fruits_0[1:0])
# []

print(fruits_0[:4])
# ['Apple', 'Banana', 'Cherry', 'Papaya']

print(fruits_0[1:])
# ['Banana', 'Cherry', 'Papaya', 'Guava']

print(fruits_0[-4:3])
# ['Banana', 'Cherry']

print(fruits_0[-4:1])
# []
# because both are same in 
# fruits_0 = ["Apple", "Banana", "Cherry", "Papaya", "Guava"]

# 4. Check if item exists in list

if "Apple" in fruits_0:
    print("Yes, Apple is in list")

print(
"""This is a fruit guess game, 
see if the entered fruit name 
exists in our pre built list:
Enter your guess > 
""")

input_value = input("")

if input_value in fruits_0:
    print(f"You are Correct! {input_value} exists in the list")
else:
    print(f"Sorry! Your guess {input_value} is wrong")
