# Write a Python program to get the volume of a sphere with radius 6.

import math
r = input("What is the radius of the sphere you want to compute the volume for?: ")
radius = float(r)
volume = (4/3)*math.pi * radius**3
print ("The volume of the sphere is {}".format(volume))
