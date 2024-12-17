# Join lists

# 1. using + operator

vegetables = ["Potato", "Tomato", "Okra"]
fruits = ['apple', 'Banana', 'cherry', 'Pomegranate']

mix = vegetables + fruits

print(mix)
# ['Potato', 'Tomato', 'Okra', 'apple', 'Banana', 'cherry', 'Pomegranate']

# 2. use append method to join

list1 = ["This", "is" , "code"]
list2 = [3, 4+2, 5+0.0]

for x in list2:
    list1.append(x)
print(list1)

# ['This', 'is', 'code', 3, 6, 5.0]

# 3. use extend method
list3 = ["a", "b" , "c"]
list4 = [1, 2, 3]

list4.extend(list3)
print(list4)
# [1, 2, 3, 'a', 'b', 'c']

