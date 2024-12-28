'''
List Histogram

Write a Python program to create a histogram from a given list of integers.

Sample Output:
**                                                                                                            
***                                                                                                           
******                                                                                                        
*****
'''

def create_hist(value):

    for i in value:
        print("*" * i)

create_hist([2,5,2,11,3])