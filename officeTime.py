# officeTime.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 2.7.  App to show if the office is open in a few different locations.
# A simple application for checking to see if certain office locations are open.

from time import gmtime, strftime

# grabbing greenwhich meantime hour and calculating other time zones for Portland & NYC and saving them to variables
# also converting time as an integer so that it can be evaluated correctly
gmHour = int(strftime("%H", gmtime()))
portHour = gmHour - 8
nyHour = gmHour - 5
# grabbing greenwhich minutes and saving it to a variable
gmMinute = int(strftime("%M", gmtime()))

# defines main function to see if the time passed in is within office hours and also converts it from military time.
def isOpen (curTime):
    # checks to see if time passed in is within office hours
    if (curTime >= 9 and curTime <= 21):
        office = "is open"
    else:
        office = "is closed"
    # checks if time passed in is above 12 hrs (military time) and then converts it to normal time if so.
    if (curTime > 12):
        amPm = "PM"
        normHour = curTime - 12
    else:
        amPm = "AM"
        normHour = curTime
    # checks which time is passed in and sets location
    if curTime is gmHour:
        location = "London"
    elif curTime is portHour:
        location = "Portland"
    else:
        location = "New York City"
    # fixes minute formatting problem where there is no '0' added with single digit minutes
    if gmMinute < 10:
        minute = '0'
    else:
        minute = ''
    # print statement puting everything together for displaying
    print "The time in %s is %s:%s%s%s. The %s office %s." %(location, normHour, minute, gmMinute, amPm, location, office)    

isOpen(portHour)
isOpen(nyHour)
isOpen(gmHour)

