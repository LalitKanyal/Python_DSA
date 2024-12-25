'''
14. Days Between Dates

Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

from datetime import date

# get the date first

first_date = date(2014, 7, 2)
# 2014-07-02

second_date = date(2014, 7, 11)
# 2014-07-11

difference_date = second_date - first_date

print(difference_date)
# 9 days, 0:00:00

print(difference_date.days)
# 9