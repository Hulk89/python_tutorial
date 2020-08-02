import wx
import gui

class MainApp(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)

        self.panelOne = Panel1(self)

class Panel1(gui.panel_one):
    def __init__(self, parent):
        gui.panel_one.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel( self, event ):
        if self.IsShown():
            # hide panel1
            self.parent.SetTitle("Panel Two Showing")
            self.Hide()
            # make panel2 and show it
            self.parent.panelTwo = Panel2(self.parent)
            self.parent.panelTwo.Show()



class Panel2(gui.panel_two):
    def __init__(self, parent):
        gui.panel_two.__init__(self, parent)
        self.parent = parent

    def changeIntroPanel( self, event ):
        # return to panelOne
        self.parent.SetTitle("Panel One Showing")
        self.parent.panelOne.Show()
        # destroy itself
        self.parent.panelTwo = None
        self.Destroy()

def main():
    app = wx.App()
    window = MainApp(None)
    window.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
