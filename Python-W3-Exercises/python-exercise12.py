# Write a Python program to print the calendar of a given month and year.

import calendar

m = int(input("Give me a month by number: "))
y = int(input("Give me a year: "))

c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(y, m)
