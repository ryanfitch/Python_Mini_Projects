# Write a Python program to find whether a given number (accept from the user)
# is even or odd, print out an appropriate message to the user.

num = int(input("Give me a number: "))
if num > 0:
    if num % 2 == 0:
        print ("This number is even.")
    elif num % 2 != 0:
        print ("This number is odd.")
else:
    print("This number is not a positive number.")
    
