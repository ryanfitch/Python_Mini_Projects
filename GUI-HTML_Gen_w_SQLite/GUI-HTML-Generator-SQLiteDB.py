# GUI-HTML-Generator-SQLiteDB.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5  GUI HTML Generator App DB
# HTML GENERATOR APP constructed with Python 3.5, tkinter and SQLite3.

from tkinter import *
import sqlite3
import webbrowser

class HTMLgenerator():

    def __init__(self, master):
        frame=Frame(master, width=80, height=50)
        frame.pack()

        # MASTER
        master.title('HTML GENERATOR')
        master.resizable(True, True)
        master.configure(background = "#e9e9e9")

        # IMAGES
        img1 = PhotoImage(file = 'Drawing.gif')
        self.openclose = img1

        
        # HEADER
        self.text = Label(frame, image = self.openclose)
        self.text.pack()
        self.text.grid(row=0, sticky=W)
        self.text["text"] = "HTML Generator"
        self.text.config(background = "#e9e9e9")

        self.lab = Label(frame, text="stuff1")
        self.lab.pack(side=LEFT)
        self.lab.grid(row=1)


        # TEXT FIELDS
        self.cont1Field = Entry(frame, text = "stuff1", width=49)
        self.cont1Field.insert(0, "Enter New <H1> Content")
        self.cont1Field.pack()
        self.cont1Field.grid(row=1)
        self.cont1Field.bind("<FocusIn>", self.clearcont1Field)
        self.cont1Field.config(background = "#faf8f8")

        self.cont2Field = Entry(frame, text = "stuff2", width=49)
        self.cont2Field.insert(0, "Optional Secondary <p> Content")
        self.cont2Field.pack()
        self.cont2Field.grid(row=2)
        self.cont2Field.bind("<FocusIn>", self.clearcont2Field)
        self.cont2Field.config(background = "#faf8f8")


        # BUTTONS
        self.btn=Button(frame, text='Add Content', command=self.add_note)
        self.btn.pack()
        self.btn.grid(row=5, rowspan=1, sticky="w")

        self.delbtn = Button(frame, text='Delete Content', command=self.del_notes)
        self.delbtn.pack()
        self.delbtn.grid(row=5, rowspan=1)

        self.htmlBtn = Button(frame, text='Save HTML', command=self.htmlbuild)
        self.htmlBtn.pack()
        self.htmlBtn.grid(row=5, rowspan=1, sticky="e")

        self.content=Listbox(master, width=50)
        self.content.pack(padx = 25, pady = 15)
        self.content.config(background = "#faf8f8")


        # OPEN DATABASE
        self.conn = sqlite3.connect('newHTMLcontent.db')

        c = self.conn.cursor()

        # CREATE TABLE
        c.execute('''CREATE TABLE IF NOT EXISTS newContent(stuff1 TEXT primary key, stuff2 TEXT)''')
        self.conn.commit()

        # ADD CONTENT DATA
        c.execute("INSERT INTO newContent VALUES('Stay tuned for our amazing summer sale!','')")
        self.conn.commit()
        
        # READ CONTENT
        newContent = c.execute("SELECT * FROM newContent")
        self.conn.commit()

        # ADD TO LIST
        for stuff in newContent:
            self.content.insert(END, stuff)

        c.close()

    def clearcont1Field(self, event):
        self.cont1Field.delete(0,END)

    def clearcont2Field(self, event):
        self.cont2Field.delete(0,END)

    def add_note(self):
        if self.cont1Field.get() == "":
            self.text["text"] = "Please add some new content:"
        else:
            item1 = self.cont1Field.get()
            item2 = self.cont2Field.get()

            self.cont1Field.delete(0, END)
            self.cont2Field.delete(0, END)

            # ADD TO DATABASE
            c = self.conn.cursor()
            c.execute("INSERT INTO newContent VALUES (?, ?)", (item1, item2))
            self.conn.commit()
            c.close()

            # ADD TO LIST
            self.content.insert(END, (item1, item2))


    def del_notes(self):
        # GET SELECTED CONTENT       
        person = self.content.get(ACTIVE)
        stuff1 = person[0]

        # DELETE IN DATABASE
        c = self.conn.cursor()
        c.execute("DELETE FROM newContent WHERE stuff1=?", [stuff1])
        self.conn.commit()
        c.close()

        # DELETE ON LIST
        self.content.delete(ANCHOR)

    def __del__(self): 
        # CLOSE DATABASE
        self.conn.close()

    def htmlbuild(self):
        person = self.content.get(ACTIVE)
        content1 = person[0]
        content2 = person[1]
        if content1 == "Enter New <H1> Content":
            content1 = ""
        elif content2 == "Optional Secondary <p> Content":
            content2 = ""

        # OUTPUT NEW INDEX.HTML
        html = open('index.html', 'w')
        newHTML = "<DOCTYPE html>\n<html lang = \'en\'>\n<meta charset = \'utf-8\'>\n<html> \n  <header>\n       <h1>{}</h1>\n<p>{}</p>\n  </header>\n</html>".format(content1, content2)
        html.write(newHTML)
        html.close()
        messagebox.showinfo(title='HTML GENERATOR', message='Your new index.html is located in the root directory!')


root = Tk()
HTMLgenerator(root)
root.mainloop()

