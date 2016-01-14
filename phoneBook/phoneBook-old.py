# phoneBook-old.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 2.7.  Phone / contact app.
# A simple phone book app made with Python and tkinter for saving and browsing contacts.

from Tkinter import *
# from phones import *

# phonelist data
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

def whichSelected () :
    print "At %s of %d" % (select.curselection(), len(phonelist))
    return int(select.curselection()[0])

# takes the values in the name and phone fields and adds them to the phonelist variable
def addEntry () :
    phonelist.append ([nameVar.get(), phoneVar.get()])
    setSelect ()

# uses the whichSelected function to update the phonelist data
def updateEntry() :
    phonelist[whichSelected()] = [nameVar.get(), phoneVar.get()]
    setSelect ()

# uses the whichSelected function to delete entries.
def deleteEntry() :
    del phonelist[whichSelected()]
    setSelect ()

def loadEntry  () :
    name, phone = phonelist[whichSelected()]
    nameVar.set(name)
    phoneVar.set(phone)

def makeWindow () :
    global nameVar, phoneVar, select
    # title('Phone Book')
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    # tkinter widget for name field
    Label(frame1, text="Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)
    #label.config(font = ('Tahoma', 16))

    # tkinter widget for phone field
    Label(frame1, text="Phone").grid(row=1, column=0, sticky=W)
    phoneVar= StringVar()
    phone= Entry(frame1, textvariable=phoneVar)
    phone.grid(row=1, column=1, sticky=W)

    # tkinter widgets for the buttons
    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2,text=" Add  ",command=addEntry)
    b2 = Button(frame2,text="Update",command=updateEntry)
    b3 = Button(frame2,text="Delete",command=deleteEntry)
    b4 = Button(frame2,text=" Load ",command=loadEntry)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT)

    # tkinter widget for displaying names and which ones are selected
    frame3 = Frame(win)     
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)
    return win

# function for showing the names and numbers in the display window widget
def setSelect () :
    phonelist.sort()
    select.delete(0,END)
    for name,phone in phonelist :
        select.insert (END, name)

win = makeWindow()
setSelect ()
win.mainloop()
