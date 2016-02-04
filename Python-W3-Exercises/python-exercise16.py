# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

number = int(input("Give me a number and I will find the difference from 17: "))
if number > 17:
    newNum = (number - 17) * 2
    print("The abosolute difference doubled is {}".format(newNum))
elif number <= 17:
    newNum = (17 - number)
    print("The difference is {}.".format(newNum))
else:
    print("I didn't understand that input")
          
    
