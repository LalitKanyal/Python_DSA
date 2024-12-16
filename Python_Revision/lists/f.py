# Loop list

# 1. loop through list

fruits = ['Muskmelon', 'Pomegranate', 'Cherry', 'Watermelon', 'Kafal', 'Hisalu']

for fruit in fruits:
    print(fruit)

# 2. loop through index number
# using range function

for i in range(len(fruits)):
    print(fruits[i])

print("\n")
# 3. while loop

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

print("\n")
# 4. loop through list comprehension

[print(x) for x in fruits]