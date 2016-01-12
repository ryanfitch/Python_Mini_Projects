# wxpython-drill.py by Ryan Fitch [http://ryan-fitch.com/]
# Python 2.7.  wxPython GUI.
# A simple GUI made with the wxPython module.

import wx

class windowClass(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        editButton = wx.Menu()
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit')
        fileButton.AppendItem(exitItem)

        panel = wx.Panel(self)

        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'File')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome', 'name')

        if nameBox.ShowModal() == wx.ID_OK:
            userName = nameBox.GetValue()


        yesNoBox = wx.MessageDialog(None, 'Do you enjoy wxPython?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()

        if yesNoAnswer == wx.ID_NO:
            userName = 'Loser!'

        chooseOneBox = wx.SingleChoiceDialog(None, 'What is your favorite color?',
                                            'Color Question',
                                            ['Blue','Yellow','Red','White'])

        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()

        wx.TextCtrl(panel, pos=(3, 100), size=(150,50))

        aweText = wx.StaticText(panel, -1, "Awesome Text", (3,3))
        aweText.SetForegroundColour('#67cddc')
        aweText.SetBackgroundColour('black')

        rlyAweText = wx.StaticText(panel, -1, "Customized Awesomeness", (3,30))
        rlyAweText.SetForegroundColour(favColor)
        rlyAweText.SetBackgroundColour('black')

        self.SetTitle('My Lovely Window, ' +userName)

        self.Show(True)

    def Quit(self, e):
        self.Close()


def main():
    app = wx.App()
    windowClass(None)
    app.MainLoop()

main()
