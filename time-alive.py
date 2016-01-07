# time-alive.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5.  Age calculator program.
# Asks for name & calculates how long some one as been alive.

def main():

    # function to calculate time alive
    def ageCalc(age):
        days = age * 365
        minutes = age * 525948     
        seconds = age * 31556926
        print("{} has been alive for {} days, {} minutes, and, {} seconds!  Holy cow!!".format(name.title(), days, minutes, seconds))
        playAgain()

    # function to check if user wants to check another person's time alive.
    def playAgain():
        again = input("Would you like to calculate someone else's age?(y/n): ").lower()
        if again == 'y':
            print("Ok, here we go again!")
            main()
        elif again == 'n':
            print("Ok, Goodbye!!")
            exit()
        else:
            print("I do not understand that input.")
            playAgain()

    print("Let's see how long someone has been alive.")
    name = input("What's their name? ")
    #error catching to make sure a number was entered
    while True:
        print("Now what's their age?")
        try:
            age = int(input("Age: "))
            ageCalc(age)
        except ValueError:
            print("That's not a number.  Give me an age number.")
        else:
            ageCalc(age)
                
if __name__ == "__main__": main()
