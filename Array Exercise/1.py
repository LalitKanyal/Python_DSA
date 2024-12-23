'''
Write a Python program to create an array of 5 integers 
& display the array items. 
Access individual elements through indexes.

Sample Output:
1
3
5
7
9

Access first three items individually
1
3
5
'''

# Solution
from array import array

# create an array of integers
int_array = array('i', [1, 3, 5, 7, 9])

# access each item of array

for i in int_array:
    print(i)

print("=" * 80)
# access first three items of array
for i in int_array[:3]:
    print(i)


# Explanation
# https://www.youtube.com/watch?v=v6jIT7rlWBM
