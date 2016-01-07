# database_basic_SQLite3_ex.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5.  Basic SQLite3 example
# Create a db in RAM, create a table with 3 columns, insert 3 rows of data, update 1 of those rows, select 2 of those rows

import sqlite3

def main():
    db = sqlite3.connect('roster.db')
    db.row_factory = sqlite3.Row
    # create db called Roster
    db.execute('drop table if exists Roster')
    # create a table with 3 columns
    db.execute('create table Roster (name text, species text, iq int)')
    # insert 3 rows of data
    db.execute('insert into Roster (name, species, iq) values (?, ?, ?)', ("Jean-Baptiste Zorg", "Human", 122))
    db.execute('insert into Roster (name, species, iq) values (?, ?, ?)', ("Korben Dallas", "Meat Popsicle", 100))
    db.execute('insert into Roster (name, species, iq) values (?, ?, ?)', ("Ak'not", "Mangalore", -5))
    db.commit()
    # display all
    cursor = db.execute('select * from Roster order by iq')
    for row in cursor:
        print(row['name'], row['species'], row['iq'])
    print (" ")
    # update 1 of those rows
    db.execute("UPDATE Roster SET Species='Human' WHERE Name='Korben Dallas'")
    db.commit()
    # select 2 of those rows and display them
    cursor = db.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
    for row in cursor:
        print(row['name'], row['iq'])

if __name__ == "__main__": main()
