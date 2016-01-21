# original script

import webbrowser
from tkinter import *
from tkinter import ttk


class HTMLgenerator:

    def __init__(self, master):

        # MASTER
        master.title('GENERATE HTML')
        master.resizable(True, True)
        master.configure(background = '#e9e9e9')

        # IMAGES
        img1 = PhotoImage(file = 'Drawing.gif')
        self.openclose = img1


        # HEADER
        self.html_frame = ttk.Frame(master)
        self.html_frame.pack(fill = BOTH, expand = 1)
        ttk.Label(self.html_frame, image = self.openclose).grid(row = 0, column = 0)
        self.mainheader = ttk.Label(self.html_frame, text = '')
        self.mainheader.grid(row = 0, column = 1)
        self.mainheader.config(background = '#f16529')


        # MAIN FRAME
        self.main = ttk.Frame(master)
        self.main.pack(fill = BOTH, expand = 2)


        # NOTEBOOK (TABS)
        self.notebook = ttk.Notebook(self.main)
        self.notebook.pack(fill = BOTH, expand = 1)


        # TABS
        self.prog = ttk.Frame(self.notebook)
        ttk.Label(self.prog, text = "Hi There!\nWelcome to my Python app.\nJust click the HTML INPUT tab \nand insert your new text.\nWhen you're feeling good about it...\nClick HTML ME! to generate the html file.").grid(row = 0, column = 0, pady = 70, padx = 77)
        # ttk.Label(self.prog, text = 'place holder 2').grid(row = 0, column = 1, padx = 10)
        self.htmltab = ttk.Frame(self.notebook)
        self.notebook.add(self.prog, text = '  OVERVIEW ')
        self.notebook.add(self.htmltab, text = '  HTML INPUT   ')

        self.headerlabel = ttk.Label(self.htmltab, text = 'Enter your new info inbetween the HTML <header> tags:')
        self.headerlabel.pack()


        # TEXT
        self.html = Text(self.htmltab, width = 55, height = 15)
        self.html.insert(1.0, '<DOCTYPE html>\n<html lang = \'en\'>\n<meta charset = \'utf-8\'>\n<html> \n  <header> \n\n<-- Your New Text Goes Here -->\n\n  </header>\n</html>')
        self.html.pack()


        # BUTTONS
        self.run = ttk.Button(self.main, text = 'HTML ME!')
        self.run.pack(side = RIGHT)
        self.clear = ttk.Button(self.main, text = 'CLEAR IT!')
        self.clear.pack(side = LEFT)


        # BIND
        self.clear.bind('<1>', lambda e: self.clear_())
        self.run.bind('<1>', lambda e: self.htmlbuild_())

    # EVENTS
    def clear_(self):
        self.html.delete(1.0, 'end')

    def clearheader_(self):
        self.html.delete(1.0, 'end')

    def htmlbuild_(self):
        html = open('index.html', 'w')
        html.write(self.html.get(0, 'end'))


def main():
    root = Tk()
    HGen = HTMLgenerator(root)
    root.mainloop()

if __name__ == '__main__': main()
