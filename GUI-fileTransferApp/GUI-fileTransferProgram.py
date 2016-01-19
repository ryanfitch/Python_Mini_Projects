# GUI-fileTransferProgram.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5  GUI File Tansfer App
# FILE TRANSFER APP constructed with Python 3.5 and tkinter.


from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import shutil, os
import datetime, time

class FileTransfer:


    def __init__(self, master):

        # MASTER SETTINGS
        master.title('FILE TRANSFER PROGRAM')
        master.resizable(False, False)
        master.configure(background = '#e9e9e9')

        self.style = ttk.Style()
        # IMAGE
        self.transfer = PhotoImage(file = 'drawing.gif')
        self.icon = self.transfer


        # HEADER
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        ttk.Label(self.header_frame, image = self.icon).grid(row = 0, column = 2, rowspan = 2)
        ttk.Label(self.header_frame, text = '').grid(row = 0, column = 3)
        ttk.Label(self.header_frame, text = '\n     FILE TRANSFER PROGRAM:\n\n'
                                            '»  Choose the file you want to transfer.\n'
                                            '»  Then choose the destination folder.\n'
                                            '»  When both paths are specified\n       click TRANSFER.\n'
                                            '»  Hit CLEAR to clear all fields.\n\n', font = ('Arial', 15)).grid(row = 2, column = 2)



        # CONTENT
        self.content = ttk.Frame(master)
        self.content.pack()

        # TITLES ABOVE FIELDS
        ttk.Label(self.content, text = 'FILE PATH:',font = ('sys', 11,'bold')).grid(row = 0, column = 0, padx = 5, sticky = 'nw')
        ttk.Label(self.content, text = 'FILE DESTINATION PATH:', font = ('sys', 11,'bold')).grid(row = 0, column = 1, padx = 5, sticky = 'nw')
        ttk.Label(self.content, text = 'COMMENTS:', font = ('sys', 11,'bold')).grid(row = 3, column = 0, sticky = 'nw', padx = 5)

        # ENTRY FIELDS
        self.file_entry = ttk.Entry(self.content, width = 25, font = ('Ariel', 8))
        self.file_entry.grid(row = 0, column = 0, padx = 5, sticky = 'ne')
        self.file_dest = ttk.Entry(self.content, width = 34, font = ('Ariel', 8))
        self.file_dest.grid(row = 0, column = 1, padx = 5, sticky = 'ne')
        self.comments = Text(self.content, width = 80, height = 10)
        self.comments.grid(row = 4, column = 0, columnspan = 2)


        # BUTTONS
        self.browse = ttk.Button(self.content, text = 'BROWSE')
        self.browse.grid(row = 2, column = 0, sticky = 'nw', padx = 5, pady = 4)
        self.browse2 = ttk.Button(self.content, text = 'BROWSE')
        self.browse2.grid(row = 2, column = 1, sticky = 'nw', padx = 5, pady = 4)
        self.clear = ttk.Button(self.content, text = 'CLEAR')
        self.clear.grid(row = 5, column = 0, sticky = 'ne',pady = 5, padx = 5)
        self.transfer = ttk.Button(self.content, text = 'TRANSFER')
        self.transfer.grid(row = 5, column = 1, sticky = 'nw', padx = 90, pady = 5)
        self.cancel = ttk.Button(self.content, text = 'CANCEL', command = quit).grid(row = 5, column = 1, sticky = 'nw', pady = 5, padx = 0)


        # PROGRESS BAR
        value = IntVar()
        self.prog = ttk.Progressbar(self.content, orient = HORIZONTAL, length = 250, maximum = 50.0, value = 0)


        # BIND EVENTS
        self.transfer.bind('<1>', lambda e: self.transfer_())
        self.clear.bind('<1>', lambda e: self.clear_())
        self.browse.bind('<1>', lambda e: self.browse_())
        self.browse2.bind('<1>', lambda e: self.browse2_())


    # DEFINE EVENTS
    def transfer_(self):
        path = self.file_entry.get()
        dest = self.file_dest.get()
        shutil.copy(path, dest)
        self.clear_()
        mb.showinfo(title='FILE TRANSFER', message='File transferred to %s' %dest)


    def browse_(self):
        dirname = fd.askopenfilename()
        self.file_entry.delete(0, 'end')
        self.file_entry.insert(0, dirname)

    def browse2_(self):
        destname = fd.askdirectory()
        self.file_dest.delete(0, 'end')
        self.file_dest.insert(0, destname)


    def clear_(self):
        self.file_entry.delete(0,'end')
        self.file_dest.delete(0,'end')



def main():
    root = Tk()
    FT = FileTransfer(root)
    root.mainloop()

if __name__ == '__main__': main()
