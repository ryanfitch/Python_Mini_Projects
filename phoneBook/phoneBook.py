# phoneBook.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5.  Phone / contact app.
# A simple phone book app made with Python and tkinter for saving and browsing contacts.


from tkinter import *
from tkinter import ttk

root=Tk()

# Phone Book title
label = ttk.Label(root, text = "     Phone Book")
label.pack(fill = BOTH, expand = True, padx=10, pady=10)
label.config(foreground = 'black', background = '#e9e9e9')
label.config(font = ('Tahoma', 35, 'bold'))

# sets up panedwindow frames
panedwindow = ttk.Panedwindow(root, orient = VERTICAL)
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
labelNumber = ttk.Label(frameLeft, text = "Number:")
labelName.pack(fill = BOTH, expand = True)
labelNumber.pack(fill = BOTH, expand = True)

nameEntry = ttk.Entry(frameRight, width = 15)
nameEntry.pack(fill = BOTH, expand = True)
phoneEntry = ttk.Entry(frameRight, width = 15)
phoneEntry.pack(fill = BOTH, expand = True)

b1 = Button(frame2, text = "Add")
b2 = Button(frame2, text = "Update")
b3 = Button(frame2, text = "Delete")
b4 = Button(frame2, text = "Load")

b1.pack(side=LEFT, padx=10, pady=5)
b2.pack(side=LEFT, padx=10, pady=5)
b3.pack(side=LEFT, padx=10, pady=5)
b4.pack(side=LEFT, padx=10, pady=5)

logo = PhotoImage(file = 'phone.gif') # change path to image as necessary
label.config(image = logo)
# sets which image and text is displayed
label.config(compound = 'text')
label.config(compound = 'left')

label.img = logo
label.config(image = label.img)

root.mainloop()
