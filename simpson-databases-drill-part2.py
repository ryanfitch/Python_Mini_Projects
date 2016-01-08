# simpson-databases-drill.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 2.7
# Python program which uses the Simpsons characters as data for creating a new table, adding new characters, viewing all character details, viewing specific character details, and deleting a character.



import sqlite3

# Connect to simpsons database
conn = sqlite3.connect('simpsons.db')

def createTable():
    conn.execute("CREATE TABLE if not exists \
        SIMPSON_INFO( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        NAME TEXT, \
        GENDER TEXT, \
        AGE INT, \
        OCCUPATION TEXT \
        );")
    
def printData(data):
    for row in data:
        print "Id:", row[0]
        print "Name:", row[1]
        print "Gender:", row[2]
        print "Age:", row[3]
        print "Occupation:", row[4], "\n"

def newCharacter():
    print '\nAdding a new character...'
    
    # Take inputs
    name = raw_input('Name: ')
    gender = raw_input('Gender: ')
    age = raw_input('Age: ')
    occupation = raw_input('Occupation: ')
    
    # Create values part of sql command
    val_str = "'{}', '{}', {}, '{}'".format(\
        name, gender, age, occupation)
    
    sql_str = "INSERT INTO SIMPSON_INFO \
        (NAME, GENDER, AGE, OCCUPATION) \
        VALUES ({});".format(val_str)
    print sql_str
    
    conn.execute(sql_str)
    conn.commit()
    print "Number of changes:", conn.total_changes
    
def viewAll():
    # Create sql string
    sql_str = "SELECT * from SIMPSON_INFO"
    cursor = conn.execute(sql_str)
    
    # Get data from cursor in array
    rows = cursor.fetchall()
    print rows

def viewDetails():
    print "\nViewing character details"
    
    # Take name input
    name = raw_input("Enter the character's name: ")
    sql_str = "SELECT * from SIMPSON_INFO where NAME='{}'"\
        .format(name)
    
    cursor = conn.execute(sql_str)
    
    # Get data in array form
    rows = cursor.fetchall()
    if len(rows) == 0:
        # There is no data in array
        print 'No records found'
    else:
        # Print the data
        printData(rows)
        
def deleteCharacter():
    print "\nDeleting a Character"
    
    # Take name input
    name = raw_input("Enter the character's name: ")
    sql_str = "SELECT * from SIMPSON_INFO where NAME='{}'"\
        .format(name)
    
    cursor = conn.execute(sql_str)
    
    # Get data in array form
    rows = cursor.fetchall()
    # ID to change
    change_id = 0
        
    if len(rows) == 0:
        print 'No records found'
        # End the function
        return
    elif len(rows) == 1:
        print 'One record found'
        # Select row
        row = rows[0]
        # Select Id
        change_id = row[0]
        printData(rows)
    else:
        print 'More than one record found...'
        printData(rows)
        change_id = raw_input(\
        'Type the ID of the character to update: ')
    
    print "Change ID:", change_id
    
    delete = raw_input("Confirm character delete (y/n): ")
    
    if delete == "y":
        sql_str = "DELETE from SIMPSON_INFO where ID={}"\
                  .format(change_id)
        conn.execute(sql_str)
        conn.commit()
        print "Number of changes: ", conn.total_changes

def updateCharacter():
    print "\nUpdating a Character"
    
    # Take name input
    name = raw_input("Enter the character's name: ")
    sql_str = "SELECT * from SIMPSON_INFO where NAME='{}'"\
        .format(name)
    
    cursor = conn.execute(sql_str)
    
    # Get data in array form
    rows = cursor.fetchall()
    # ID to change
    change_id = 0
        
    if len(rows) == 0:
        print 'No records found'
        # End the function
        return
    elif len(rows) == 1:
        print 'One record found'
        # Select row
        row = rows[0]
        # Select Id
        change_id = row[0]
        printData(rows)
    else:
        print 'More than one record found...'
        printData(rows)
        change_id = raw_input(\
        'Type the ID of the character to update: ')
    
    print "Change ID:", change_id
    
    print 'Insert the updated information:'
    
    # Get change data
    name = raw_input('Name: ')
    gender = raw_input('Gender: ')
    age = raw_input('Age: ')
    occupation = raw_input('Occupation: ')
    
    if not name == '':
        sql_str = "UPDATE SIMPSON_INFO \
            set NAME='{}' where ID={}" \
            .format(name, change_id)
        conn.execute(sql_str)
    if not gender == '':
        sql_str = "UPDATE SIMPSON_INFO \
            set GENDER='{}' where ID={}" \
            .format(gender, change_id)
        conn.execute(sql_str)
    if not age == '':
        sql_str = "UPDATE SIMPSON_INFO \
            set AGE={} where ID={}" \
            .format(age, change_id)
        conn.execute(sql_str)
    if not occupation == '':
        sql_str = "UPDATE SIMPSON_INFO \
            set OCCUPATION='{}' where ID={}" \
            .format(occupation, change_id)
        conn.execute(sql_str)
    
    conn.commit()
    print "Number of changes: ", conn.total_changes
    
    sql_str = "SELECT * from \
        SIMPSON_INFO where ID={}" \
        .format(change_id)
    
    cursor = conn.execute(sql_str)
    
    # Get data in array form
    rows = cursor.fetchall()
    printData(rows)

def options():
    # Print out the options
    print '\nWhat would you like to do?'
    print '1. Add a new character'
    print '2. View all characters'
    print '3. Search for a character'
    print '4. Delete a character'
    print '5. Update a character'
    print '6. Exit'
    
    # Ask user what they want to do
    response = raw_input('Enter your option number: ')
    
    # Check the user response
    if response == '1':
        newCharacter()
    elif response == '2':
        viewAll()
    elif response == '3':
        viewDetails()
    elif response == '4':
        deleteCharacter()
    elif response == '5':
        updateCharacter()
    else:
        print 'Exiting the program'
        return

def mainLoop():
    in_loop = True
    while in_loop == True:
        # Run options function
        options()
        # Ask user if they want to continue
        again = raw_input(\
        'Would you like to do something else? (y/n) ')
        # if answer does not equal 'y', exit loop
        if again != 'y':
            in_loop = False

createTable()
mainLoop()
