# Write a Python program which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers.

numbers = input("Give me a list of numbers separated by commas: ")

list = numbers.split(",")
newList = [i.replace(' ','') for i in list]
tup = tuple(newList)
print ("List: ",newList)
print ("Tuple: ",tup)


