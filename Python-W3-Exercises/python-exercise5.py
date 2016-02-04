# Write a Python program which accept the user's first and last name
# and print them in reverse order with a space between them.

firstName = input("What is your full name?")
revName = firstName[::-1]
print ("Your name backwards is : {}".format(revName.title()))
