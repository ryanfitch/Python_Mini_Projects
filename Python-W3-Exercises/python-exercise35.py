# Write a Python program that will return true if the two given
# integer values are equal or their sum or difference is 5.

val1 = int(input("Give me a number: "))
val2 = int(input("Give me another number: "))

if val1 == val2:
    print("True")
elif (val1 - val2 == 5):
    print(val1 + val2)
elif (val2 - val1 == 5):
    print(val1 + val2)
else:
    print("Not sure what to do")
    
