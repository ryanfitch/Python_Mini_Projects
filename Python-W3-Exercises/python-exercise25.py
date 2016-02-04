# Write a Python program to check whether a specified value is
# contained in a group of values.

def check_num (value):
    list = [1, 5, 8, 3]
    for num in list:
        if value == num:
            print("True")
    print ("False")

number = int(input("Give me a number: "))
check_num(number)
