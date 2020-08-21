import wx

class MyFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, id=wx.ID_ANY, title=wx.EmptyString,
                         pos=wx.DefaultPosition, size=wx.Size(600 ,600))

        self.logger = wx.TextCtrl(self, 5, "", wx.Point(20,20), wx.Size(200,200), wx.TE_MULTILINE)

    def AddText(self):
        self.logger.Clear()
        self.logger.AppendText("a\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\n")

app = wx.App()
frame = MyFrame(None) 
frame.Show(1)
frame.AddText()

app.MainLoop()
