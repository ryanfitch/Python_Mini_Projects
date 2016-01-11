# number_game.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5.  Number game.
# A simple number game where you get 3 chances to pick the right number from 1 to 10.

import random

def main():
    misses = 0

    def lives():
        if misses < 3:
            print ("you have missed {} times".format(misses))
        elif misses == 3:
            print("you missed 3 times.  you lose!")
            playagain()

    def playagain():
        again = input("would you like to play again? y/n  ")
        if again == 'y':
            main()
        elif again == 'n':
            print("goodbye!...")
            exit()
        else:
            print("i don't understand that input. would you like to play again? y/n  ")
            playagain()

    def welcome():
        print(" ")
        print(" ")
        print(" ")
        print("hello.  welcome to my number game.")
        print("you only get 3 chances to guess the right number")
        print("let's play!")
        print(" ")
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)

    welcome()
    while True:
        try:
            # get a number guess from the player
            guess = int(input("guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            if guess < secret_num:
                print("too low")
                misses += 1
                lives()
                print("choose again please...")
            elif guess > secret_num:
                print("too high")
                misses += 1
                lives()
                print("choose again please...")
            elif guess == secret_num:
                print("yes, the number was {}.  you nailed it!!".format(secret_num)) 
                playagain()

if __name__ == "__main__": main()
  
