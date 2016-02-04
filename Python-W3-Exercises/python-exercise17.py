# Write a Python program to test whether a number is within 100 of 1000 or 2000.

num = int(input("Give me a number: "))

if num > 900 and num < 1100:
    print ("{} is within 100 of 1000".format(num))
elif num > 1900 and num < 2100:
    print ("{} is within 100 of 2000".format(num))
else:
    print ("{} is not within 100 of 1000 or 2000".format(num))
