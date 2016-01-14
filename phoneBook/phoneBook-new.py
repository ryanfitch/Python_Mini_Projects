# phoneBook2.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 3.5.  Phone / contact app.
# A simple phone book app made with Python and tkinter for saving and browsing contacts.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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

nameList = [name[0] for name in phonelist]


class Phonebook:

    def __init__(self, master):

        master.title('Phone Book')
        master.resizable(False, False)
        master.configure(background = '#e9e9e9')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e9e9e9')
        self.style.configure('TButton', background = '#e9e9e9')
        self.style.configure('TLabel', background = '#e9e9e9', font = ('Tahoma', 14))
        self.style.configure('Header.TLabel', font = ('Tahoma', 40, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file = 'phone.gif')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, columnspan = 1, padx = 15, pady = 15)
        ttk.Label(self.frame_header, text = "Phone Book", style = 'Header.TLabel').grid(row = 0, column = 2, columnspan = 3, padx = 15, pady = 15)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 1, padx = 5, sticky = 'e')
        ttk.Label(self.frame_content, text = 'Number:').grid(row = 1, column = 1, padx = 5, sticky = 'e')
        # ttk.Label(self.frame_content, text = 'Notes:').grid(row = 2, column = 1, padx = 5, sticky = 'e')

        self.entry_name = ttk.Entry(self.frame_content, width = 16)
        self.entry_number = ttk.Entry(self.frame_content, width = 16)
        # self.entry_notes = ttk.Entry(self.frame_content, width = 12)
        self.text_addressBook = Text(self.frame_content, width = 30, height = 20, font = ('Tahoma', 12))

        ttk.Button(self.frame_content, text = 'Add', command = self.add).grid(row = 4, column = 0, padx = 3, pady = 10)
        ttk.Button(self.frame_content, text = 'Update').grid(row = 4, column = 1, padx = 3, pady = 10)
        ttk.Button(self.frame_content, text = 'Delete', command = self.clear).grid(row = 4, column = 2, padx = 3, pady = 10)
        ttk.Button(self.frame_content, text = 'Find').grid(row = 4, column = 3, padx = 3, pady = 10)
        
        self.entry_name.grid(row = 0, column = 2,  columnspan = 3, padx = 5, sticky = 'w')
        self.entry_number.grid(row = 1, column = 2,  columnspan = 3, padx = 5, sticky = 'w')
        # self.entry_notes.grid(row = 2, column = 2, padx = 5)
        self.text_addressBook.grid(row = 5, column = 0, columnspan = 4, padx = 0)
        self.text_addressBook.insert(INSERT, nameList)

        # self.treeview = ttk.Treeview(master)        
        # self.treeview.pack()
        # self.treeview.config(columns = ('version'))
        # self.treeview.insert('', '0', 'nameLabel', text = 'Name:')
        # self.treeview.insert('version', '0', 'nameLabel', text = 'Number:')
        # self.treeview.heading('', text = 'number:')

    def whichSelected (self):
        # print ("At {} of {}".format(select.curselection(), len(phonelist))
        # return int(select.curselection()[0])
        pass
               
    def add(self):
        # phonelist.append([nameVar(), phoneVar.get()])
        phonelist.append([self.entry_name.get(), self.entry_number.get()])
        # print('Name: {}'.format(self.entry_name.get()))
        # print('Number: {}'.format(self.entry_number.get()))
        # print('Notes: {}'.format(self.entry_notes.get()))
        nameList = [name[0] for name in phonelist]
        messagebox.showinfo(title = 'Add Feedback', message = 'Entry added!')
        self.text_addressBook.delete('1.0', 'end')
        self.text_addressBook.insert(INSERT, nameList)
        
    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_number.delete(0, 'end')
        self.entry_notes.delete(0, 'end')

    def phonelistName(self):
        name_view = phonelist.keys()
        names = list(name_view)
        names

def main ():

    root = Tk()
    setSelect (root)
    root.mainloop()

if __name__=="__main__": main()
        
