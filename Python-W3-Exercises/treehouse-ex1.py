# program which takes a string and makes the first half of the string lowercase and the second half uppercase.

def sillycase(string):
    length = round((len(string))/2)
    firstHalf = string[:length]
    secondHalf = string[length:]
    newWord = (firstHalf.lower() + secondHalf.upper())
    print(newWord)

sillycase("This is my new sentence to change.")

