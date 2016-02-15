# create a function named word_count() that takes a string and returns a dictionary with each word in the string as the key and the number of times it appears as the value


def word_count(my_string):
    string_dict={}
    for word in my_string.split():
        if word in string_dict:
            string_dict[word]+=1
        else:
            string_dict[word]=1
    print(string_dict)

word_count("Here's my string to test. My string has a few words to test.")

