# Python Dates

import datetime

t = datetime.datetime.now()
# module class method
print(t)

# 2024-12-25 08:13:13.782596
# year month day hour minute seconds microsecond

print(t.year)
print(t.month)
print(t.strftime("%d/%m/%y"))
print(t.strftime("%A"))

# ----- Create date object -----
# datetime requires three parameters - year, month, day

y = datetime.datetime(2024, 12, 23)
print(y)


# strftime() method 
# used for formatting date objects into strings
# it takes a parameter

z = datetime.date(2021, 3, 23)

# Day
print(z.strftime("%A"))

# Month
print(z.strftime("%B"))

# weekday
print(z.strftime("%w"))

# year
print(z.strftime("%Y"))