# scraping-web-html.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 2.7
# Python exercise to scrape web HTML data and extract member names from a website

import urllib2
from bs4 import BeautifulSoup

# Open webpage
webpage = urllib2.urlopen ( \
    "http://inadaybooks.com/justiceleague")

# Displays all HTML data
# print BeautifulSoup(webpage)

# Convert to BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Displays HTML title
# print soup.title
# Displays all the HTML data in the body tag
# print soup.body

# Get the contents container div
divContainer = soup.find("div", {"id":"container"})
# print divContainer

divBlock = divContainer.findAll("div", \
                                {"class":"block"})
# print divBlock[3]

divSep = divBlock[3].findAll("div", \
                             {"class":"separator"})
# print divSep[3]

members = divSep[3].findAll("a")
# print members

# Loop through members
for member in members:
    # Strip <a>  tags
    # print member.get_text()  # displays superhero name and actor
    print member.get("title") # displays just superhero name
