# Pig_Latin.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 2.5  A program which turns anyword into pig latin.


def main():

    pyg = 'ay'
    
    def plMe():
        original = raw_input('Give me a word to turn into Pig Latin: ')

        # check to make sure we indeed have a word.  if we don't it will print 'empty'
        if len(original) > 0 and original.isalpha():
            # changes all letters to lowercase
            word = original.lower()
            # moves first letter to a new variable
            first = word[0]
            # concatenates the original word with the first letter with 'ay'
            new_word = word + first + pyg
            # shifts new_word to start on second letter
            new_word = new_word[1:len(new_word)]
            # displays the pig latin converted word
            print "This word turned into Pig Latin is %s!" %new_word
            playAgain()
        else:
            print "I didn't undertand that input.  Please try again."
            plMe()

    def playAgain():
        again = raw_input('Would you like to try another word? (y/n): ')
        if again == 'y':
            plMe()
        elif again == 'n':
            print "Ok, Goodbye!"
            exit()
        else:
            print "I didn't understand that input.  Please try again."
            playAgain()

    print "Pig Latin takes the first consonant (or consonant cluster) of an\nEnglish word, moves it to the end of the word and suffixes an ay."

    plMe()

if __name__ == "__main__": main()
