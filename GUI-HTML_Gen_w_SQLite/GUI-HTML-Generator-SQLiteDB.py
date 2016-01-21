# GUI-HTML-Generator-SQLiteDB.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5  GUI HTML Generator App
# HTML GENERATOR APP constructed with Python 3.5, tkinter and SQLite3.

import webbrowser
from tkinter import *
from tkinter import ttk
import sqlite3


class HTMLgenerator:

    def __init__(self, master):

        #MASTER
        master.title('HTML GENERATOR')
        master.resizable(True, True)
        master.configure(background = 'black')

        #IMAGES
        img1 = PhotoImage(file = 'Drawing.gif')
        self.openclose = img1

        #HEADER
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack(fill = BOTH, expand = 1)
        #self.header_frame.config
        ttk.Label(self.header_frame, image = self.openclose).grid(row = 0, column = 0)
        self.mainheader = ttk.Label(self.header_frame, text = '')
        self.mainheader.grid(row = 0, column = 1)
        self.mainheader.config(background = 'white')


        #MAIN FRAME
        self.main = ttk.Frame(master)
        self.main.pack(fill = BOTH, expand = 2)


        #NOTEBOOK (TABS)
        self.notebook = ttk.Notebook(self.main)
        self.notebook.pack(fill = BOTH, expand = 1)

        #TABS
        self.prog = ttk.Frame(self.notebook)
        ttk.Label(self.prog, text = "Hi There!\nWelcome to my Python app.\nJust click the HTML INPUT tab \nand insert your new text.\nWhen you're feeling good about it...\nClick HTML ME! to generate the html file.").grid(row = 0, column = 0, pady = 70, padx = 77)

        self.headertab = ttk.Frame(self.notebook)
        self.bodytab = ttk.Frame(self.notebook)
        self.notebook.add(self.prog, text = 'OVERVIEW')
        self.notebook.add(self.headertab, text = 'CONTENT DB')
        self.notebook.add(self.bodytab, text = 'HTML')

        self.headerlabel = ttk.Label(self.headertab, text = 'Database placeholder:')
        self.headerlabel.pack()


        #TEXT
        self.header = Text(self.headertab, width = 55, height = 15)
        self.header.insert(1.0, 'place holder')
        self.header.pack()
        self.body = Text(self.bodytab, width = 55, height = 15)
        self.body.insert(1.0, '<DOCTYPE html>\n<html lang = \'en\'>\n<meta charset = \'utf-8\'>\n<html> \n  <header> \n\n  </header>')
        self.body.pack()


        #BUTTONS
        self.run = ttk.Button(self.main, text = 'GENERATE MY NEW HTML!')
        self.run.pack(side= RIGHT)
        self.headerclear = ttk.Button(self.headertab, text = 'INSERT CONTENT')
        self.headerclear.pack(side = RIGHT, padx = 101)
        self.bodyclear = ttk.Button(self.bodytab, text = 'CLEAR')
        self.bodyclear.pack(side = RIGHT, padx = 101)


        #BIND
        self.clear.bind('<1>', lambda e: self.clear_())
        self.headerclear.bind('<1>', lambda e: self.clearheader_())
        self.bodyclear.bind('<1>', lambda e: self.clearbody_())
        self.footerclear.bind('<1>', lambda e: self.clearfooter_())
        self.cssclear.bind('<1>', lambda e: self.clearcss_())
        self.jsclear.bind('<1>', lambda e: self.clearjs_())

    #EVENTS
    def clear_(self):
        self.header.delete(1.0, 'end')
        self.body.delete(1.0, 'end')
        self.footer.delete(1.0, 'end')
        self.css.delete(1.0, 'end')
        self.js.delete(1.0, 'end')

    def clearheader_(self):
        self.header.delete(1.0, 'end')

    def clearbody_(self):
        self.body.delete(1.0, 'end')

    def htmlbuild_(self):
        html = open('html.html', 'w')
        html.write(self.header.get(0, 'end'))


def main():
    root = Tk()
    HGen = HTMLgenerator(root)
    root.mainloop()

if __name__ == '__main__': main()
