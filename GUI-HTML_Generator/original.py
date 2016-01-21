import webbrowser
from tkinter import *
from tkinter import ttk



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
        self.mainheader = ttk.Label(self.header_frame, text = 'Create a custom HTML website using CSS and JavaScript.\n'
                                                              '\t\tCODE and CLICK!')
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
        ttk.Label(self.prog, text = '\tCreate websites in one easy location.\n'
                                    'Use the tabs to navigate the main parts of an HTML page,\n'
                                    'including CSS and JavaScript for added functionality.\n\n'
                                    '\tSimply place your code in the assigned tab and \nclick [RUN].'
                                    'The program will compile your code into an \nHTML document.\n\n'
                                    '\tAfter the program has constructed your code,\n'
                                    'your browser, (Chrome, Firefox, IE), will open and display\n'
                                    'the functioning HTML page you have created.').grid(row = 0, column = 0, pady = 40, padx = 5)
        ttk.Label(self.prog, text = '\tHTML References:  \nhttp://www.w3schools.com/html/\n\n'
                                    '\tCSS References: \nhttp://www/w3schools.com/css/\n\n'
                                    '\tJavaScript references: \nhttp://www.w3schools.com/js/').grid(row = 0, column = 1, padx = 10)
        self.headertab = ttk.Frame(self.notebook)
        self.bodytab = ttk.Frame(self.notebook)
        self.footertab = ttk.Frame(self.notebook)
        self.csstab = ttk.Frame(self.notebook)
        self.jstab = ttk.Frame(self.notebook)
        self.notebook.add(self.prog, text = 'OVERVIEW')
        self.notebook.add(self.headertab, text = 'Header')
        self.notebook.add(self.bodytab, text = 'Body')
        self.notebook.add(self.footertab, text = 'Footer')
        self.notebook.add(self.csstab, text = 'CSS')
        self.notebook.add(self.jstab, text = 'JavaScript')

        self.headerlabel = ttk.Label(self.headertab, text = 'ENTER HEADER INFORMATION AND CSS/JavaScript LINKS:')
        self.headerlabel.pack()

        self.bodylabel = ttk.Label(self.bodytab, text = 'ENTER BODY CONTENT (use HTML tags):')
        self.bodylabel.pack()

        self.footerlabel = ttk.Label(self.footertab, text = 'ENTER FOOTER INFORMATION:')
        self.footerlabel.pack()

        self.csslabel = ttk.Label(self.csstab, text = 'ENTER CSS STYLING:')
        self.csslabel.pack()

        self.jslabel = ttk.Label(self.jstab, text = 'ENTER JavaScript AND jQuery FUNCTIONS:')
        self.jslabel.pack()

        #TEXT
        self.header = Text(self.headertab, width = 55, height = 15)
        self.header.insert(1.0, '<DOCTYPE html>\n<html lang = \'en\'>\n<meta charset = \'utf-8\'>\n<html> \n  <header> \n\n  </header>')
        self.header.pack()
        self.body = Text(self.bodytab, width = 55, height = 15)
        self.body.insert(1.0, '<body> \n\n\n\n\n\n\n\n\n\n</body>')
        self.body.pack()
        self.footer = Text(self.footertab, width = 55, height = 15)
        self.footer.insert(1.0, '<footer> \n\n\n\n\n\n</footer>\n </html>')
        self.footer.pack()
        self.css = Text(self.csstab, width = 55, height = 15)
        self.css.pack()
        self.js = Text(self.jstab, width = 55, height = 15)
        self.js.pack()


        #BUTTONS
        self.run = ttk.Button(self.main, text = 'RUN')
        self.run.pack(side= RIGHT)
        self.clear = ttk.Button(self.main, text = 'CLEAR ALL')
        self.clear.pack(side = RIGHT)
        self.headerclear = ttk.Button(self.headertab, text = 'CLEAR')
        self.headerclear.pack(side = RIGHT, padx = 101)
        self.bodyclear = ttk.Button(self.bodytab, text = 'CLEAR')
        self.bodyclear.pack(side = RIGHT, padx = 101)
        self.footerclear = ttk.Button(self.footertab, text = 'CLEAR')
        self.footerclear.pack(side = RIGHT, padx = 101)
        self.cssclear = ttk.Button(self.csstab, text = 'CLEAR')
        self.cssclear.pack(side = RIGHT, padx = 101)
        self.jsclear = ttk.Button(self.jstab, text = 'CLEAR')
        self.jsclear.pack(side = RIGHT, padx = 101)

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

    def clearfooter_(self):
        self.footer.delete(1.0, 'end')

    def clearcss_(self):
        self.css.delete(1.0, 'end')

    def clearjs_(self):
        self.js.delete(1.0, 'end')

    def htmlbuild_(self):
        html = open('html.html', 'w')
        html.write(self.header.get(0, 'end'))



def main():
    root = Tk()
    HGen = HTMLgenerator(root)
    root.mainloop()

if __name__ == '__main__': main()
