# Write a Python program which accept the radius of a circle from the user
# and compute the area.

import math

r = input("What is the radius you want to compute the area for?: ")
radius = float(r)
area = (math.pi * radius**2)
print ("The area is {}".format(area))
