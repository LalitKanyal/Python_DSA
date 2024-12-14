'''
Two types of loops -

while loops
for loops

While Loops -
    while condition:
        body

        
        

For Loops -
Python's for-loop syntax is a more convenient alternative to a while loop when iterating through a series of elements.

'''



# while

a = 1
while a < 11:
    print (a)
    a += 1

# break statement

b = 1
while b < 11:
    print(b)
    if b == 3:
        break
    b += 1

# continue statement

c = 1
while c < 6:
    c += 1
    if c == 5:
        continue
    print(c)

# For Loops
colors = ["red", "green", "blue", "orange", "yellow"]

for color in colors:
    print(color)

# Loop through string
for y in "yumyumyumyum":
    print(y)

# break statement in for loop

for color in colors:
    print(color)
    if color == "orange":
        break
'''
red
green
blue
orange
'''

print("    ")

for color in colors:
    if color == "orange":
        break
    print(color)

'''
red
green
blue
'''

# nested loop

colors = ["red", "yellow", "pink"]
items = ["ball", "stick", "coke"]

for color in colors:
    for item in items:
        print(color, item)