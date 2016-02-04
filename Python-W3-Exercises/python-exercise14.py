"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

from datetime import date
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)
num = date2 - date1
print("The first date is {}.".format(date1))
print("The second date is {}.".format(date2))
print("The amount of days between the two dates is {}.".format(num.days))
