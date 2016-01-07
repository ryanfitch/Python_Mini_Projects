# csv-export-to-spreadsheet.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 2.7
# CSV: Exporting data from Python to a spreadsheet

import os, csv

# The path to the script
currentPath = os.path.dirname( \
    os.path.abspath("__file__"))
print currentPath

# Make the spreadsheet path
outputCsv = currentPath + '/spreadsheet.csv'
print outputCsv

# Open the file
csvFile = open(outputCsv, "wb")

# Writing to the file (did not work)
#csvFile.write('Testing, Is there text, Hello world?')

# Create writer object
writer = csv.writer(csvFile, delimiter=',')

# Data to go in csv
row_1 = [1, "Row 1", 123]
row_2 = [2, "Row 2", 456]
row_3 = [3, "Row 3", 789]

# Write rows to csv
writer.writerow(row_1)
writer.writerow(row_2)
writer.writerow(row_3)

# Faster ways to write rows to csv if there are lots of data
# rows = [row_1, row_2, row_3]
# Or this way...
# for row in rows:
#    writer.writerow(row)
