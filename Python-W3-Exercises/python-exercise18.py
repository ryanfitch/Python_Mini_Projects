# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum.

print("Give me three numbers")
num1 = int(input("Number 1 = :"))
num2 = int(input("Number 2 = :"))
num3 = int(input("Number 3 = :"))
if num1 == num2 and num1 == num3:
    newNum = (num1 + num2 + num3) *3
    print(newNum)
else:
    print(num1 + num2 + num3)
