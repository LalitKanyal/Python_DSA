'''
22. Count 4 in List

Write a Python program to count the number 4 in a given list.
'''

# pseudocode

# list
# each element in list for loop with range len of list
# if element == 4, count and store it in variable

def calc_4(a_list):
    counter = 0
    list_length = len(a_list)
    for i in range (list_length):
       if a_list[i] == 4:
           counter += 1
    return counter

aa_list = [2,3,4,5,6,4,4,4,4]
print(calc_4(aa_list))
        
