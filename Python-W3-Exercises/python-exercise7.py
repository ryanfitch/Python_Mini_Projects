# Write a Python program to accept a filename from the user
# print the extension of that.

fileName = input("Input the file name: ")
fileExtension = fileName.split(".")
print ("The file extension is: {}".format(repr(fileExtension[-1])))
