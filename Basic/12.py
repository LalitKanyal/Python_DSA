'''
12. Monthly Calendar Display

Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
'''

import calendar

print(calendar.DECEMBER)
# returns 12

# Get calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

print(calendar.month(year, month))

# if year = 2024 and month = 12
# returns 
'''
Enter the year: 2024
Enter the month: 12
   December 2024
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
'''