# simpson-databases-drill.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 2.7
# Python program to create a simpsons database with SQLite3, creates table, inserts Simpsons charter data into the table and selects & displays some of that data. 

import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Create table named SIMPSON_INFO
conn.execute("CREATE TABLE SIMPSON_INFO( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    NAME TEXT, \
    GENDER TEXT, \
    AGE INT, \
    OCCUPATION TEXT \
    );")

# Add Bart Simpson to table
conn.execute("INSERT INTO SIMPSON_INFO \
    (NAME, GENDER, AGE, OCCUPATION) VALUES \
    ('Bart Simpson', 'Male', 10, 'Student' )");

# Add Homer Simpson to table
conn.execute("INSERT INTO SIMPSON_INFO \
    (NAME, GENDER, AGE, OCCUPATION) VALUES \
    ('Homer Simpson', 'Male', 40, 'Nuclear Plant')");

# Add Lisa Simpson to table
conn.execute("INSERT INTO SIMPSON_INFO \
    (NAME, GENDER, AGE, OCCUPATION) VALUES \
    ('Lisa Simpson', 'Female', 8, 'Student')");

# Save changes
conn.commit()

# Print number of changes to database
changes = conn.total_changes
print "Number of changes:", changes

# Get data from database
cursor = conn.execute("SELECT ID, NAME, GENDER, AGE, OCCUPATION from SIMPSON_INFO")

# Extract data from cursor
rows = cursor.fetchall()
print rows

# Searching by character name
# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO where NAME='Homer Simpson'")

# Extract data from cursor
rows = cursor.fetchall()
print 'Results for Homer Simpson:'
print rows

# Make Homer Simpson's age 41
conn.execute("UPDATE SIMPSON_INFO set AGE=41 where NAME='Homer Simpson'")

# Save changes
conn.commit()

# Print number of changes
changes = conn.total_changes
print "Number of changes: ",changes
