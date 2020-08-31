import wx


class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(
            self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        bSizer1.Add(self.m_staticText1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button1 = wx.Button(
            self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button1, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.m_button1.Bind(wx.EVT_BUTTON, self.on_click)

    def __del__(self):
        pass

    def on_click(self, event):
        event.Skip()
        self.m_staticText1.SetLabel("clicked")


app = wx.App(False)
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
