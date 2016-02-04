# Write a Python program to test whether a passed letter is a vowel or not.

let = input("Give me a letter: ")
letter = let.lower()

def is_vowel(char):
    all_vowels = 'aeiou'
    if char in all_vowels:
        print ("That was a vowel.")
    else:
        print ("That letter was not a vowel.")

is_vowel(letter)


