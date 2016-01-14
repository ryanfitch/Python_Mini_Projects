# phoneBook.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5.  Phone / contact app.
# A simple phone book app made with Python and tkinter for saving and browsing contacts.

from tkinter import *
from tkinter import ttk

phonelist = [
  ['Meyers, Chris',  '343-4349'],
  ['Smith, Robert',  '689-1234'],
  ['Jones, Janet',   '483-5432'],
  ['Barnhart, Ralph','683-2341'],
  ['Nelson, Eric',   '485-2689'],
  ['Prefect, Ford',  '987-6543'],
  ['Zigler, Mary',   '567-8901'],
  ['Smith, Bob',     '689-1234']
]

def whichSelected (self):
        print ("At {} of {}".format(select.curselection(), len(phonelist))
        return int(select.curselection()[0])

def addEntry () :
    phonelist.append ([nameVar.get(), phoneVar.get()])
    setSelect ()

def updateEntry() :
    phonelist[whichSelected()] = [nameVar.get(), phoneVar.get()]
    setSelect ()

def deleteEntry() :
    del phonelist[whichSelected()]
    setSelect ()

def loadEntry  () :
    name, phone = phonelist[whichSelected()]
    nameVar.set(name)
    phoneVar.set(phone)

def makeWindow () :
    global nameVar, phoneVar, select
    win=Tk()

    # Phone Book title
    label = ttk.Label(win, text = "     Phone Book")
    label.pack(fill = BOTH, expand = True, padx=10, pady=10)
    label.config(foreground = 'black', background = '#e9e9e9')
    label.config(font = ('Tahoma', 35, 'bold'))

    # sets up panedwindow frames
    panedwindow = ttk.Panedwindow(win, orient = VERTICAL)
    panedwindow.pack(fill = BOTH, expand = True)

    frame1 = ttk.Frame(panedwindow, width = 350, height = 0, relief = GROOVE)
    frame2 = ttk.Frame(panedwindow, width = 350, height = 50, relief = GROOVE)
    frame3 = ttk.Frame(panedwindow, width = 350, height = 200, relief = SUNKEN)

    panedwindow.add(frame1, weight = 1)
    panedwindow.add(frame2, weight = 1)
    panedwindow.add(frame3, weight = 2)

    # panel/frame2 Name:/Number: area
    panedwindow2 = ttk.Panedwindow(frame2, orient = HORIZONTAL)
    panedwindow2.pack(fill = BOTH, expand = True, padx=50, pady=10)

    frameLeft = ttk.Frame(panedwindow2, width = 100, height = 75, relief = SUNKEN)
    frameRight = ttk.Frame(panedwindow2, width = 250, height = 75, relief = SUNKEN)

    panedwindow2.add(frameLeft, weight = 1)
    panedwindow2.add(frameRight, weight = 2)

    labelName = ttk.Label(frameLeft, text = "Name:")
    nameVar= StringVar()
    labelName.pack(fill = BOTH, expand = True)
               
    labelNumber = ttk.Label(frameLeft, text = "Number:")
    phoneVar= StringVar()
    labelNumber.pack(fill = BOTH, expand = True)

    nameEntry = ttk.Entry(frameRight, width = 15)
    nameEntry.pack(fill = BOTH, expand = True)
    phoneEntry = ttk.Entry(frameRight, width = 15)
    phoneEntry.pack(fill = BOTH, expand = True)

    b1 = Button(frame2, text = " Add  ", command=addEntry)
    b2 = Button(frame2, text = "Update", command=updateEntry)
    b3 = Button(frame2, text = "Delete", command=deleteEntry)
    b4 = Button(frame2, text = " Load ", command=loadEntry)

    b1.pack(side=LEFT, padx=10, pady=5)
    b2.pack(side=LEFT, padx=10, pady=5)
    b3.pack(side=LEFT, padx=10, pady=5)
    b4.pack(side=LEFT, padx=10, pady=5)

    

    logo = PhotoImage(file = 'phone.gif') 
    label.config(image = logo)
    # sets which image and text is displayed
    label.config(compound = 'text')
    label.config(compound = 'left')

    label.img = logo
    label.config(image = label.img)

win = makeWindow()
setSelect()
win.mainloop()
