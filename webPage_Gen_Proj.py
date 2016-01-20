# webPage_Gen_Proj.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5.  Simple HTML generator program.

def main():

    def welcomeMessage():
        print ("Welcome to the Web Page Generator Program.")
        print ("This program will generate an index.html file which can be viewable in a browser")
        print ("The default HTML looks like this...\n")
        print ("<html>\n   <body>\n     <h3>Stay tuned for our amazing summer sale!</h3>\n   </body>\n</html>\n")
        toDo()

    def toDo():
        user = input("Would you like to output this HTML with this message?  Or change the message?\nHit Y to output the default or hit M to change the message:: ")
        if user == 'Y':
            default = "Stay tuned for our amazing summer sale!"
            genHTML(default)
        elif user == 'M':
            message = input("What is the new message you would like instead?  ")
            genHTML(message)
        else: 
            print ("I didn't understand that input.  Please try again.")
            toDo()

    def genHTML(msg):
        print ("Your HTML looks like this...")
        html = ("<html>\n   <body>\n     <h3>{}</h3>\n   </body>\n</html>\n".format(msg))
        print (html)
        print ("Outputting file to the desktop...\n")
        with open("index.html", "w") as HTML_file:
            HTML_file.write(html)
        runAgain()

    def runAgain():
        print ("Would you like to run again?")
        run = input("Hit Y for Yes or N for No:  ")
        if run == 'Y':
            welcomeMessage()
        elif run == 'N':
            print ("Ok. Goodbye!")
            exit()
        else:
            print ("I didn't understand that input.  Please try again.")
            runAgain()

    welcomeMessage()

if __name__ == "__main__": main()
