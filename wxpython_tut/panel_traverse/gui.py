import wx

class MainFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent,
                         id=wx.ID_ANY,
                         title=wx.EmptyString,
                         pos=wx.DefaultPosition,
                         size=wx.Size(800, 600),
                         style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

class PanelWithButton(wx.Panel):
    def __init__(self, parent, title):
        super().__init__(parent,
                         id=wx.ID_ANY,
                         pos=wx.DefaultPosition,
                         size=wx.Size(800, 600),
                         style=wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)
        self.b_button = wx.Button(self, wx.ID_ANY, u"backward", wx.DefaultPosition, wx.DefaultSize, 0)
        self.f_button = wx.Button(self, wx.ID_ANY, u"forward", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.b_button, 1, wx.ALL, 5)
        bSizer5.Add(self.f_button, 1, wx.ALL, 5)
        self.SetSizer(bSizer5)
        self.Layout()
        # Connect Events
        self.b_button.Bind(wx.EVT_BUTTON, self.backward)
        self.f_button.Bind(wx.EVT_BUTTON, self.forward)
        # set title
        self.title = title

    def __del__( self ):
        pass

    # Virtual event handlers, overide them in your derived class
    def backward(self, event):
        raise NotImplementedError

    def forward(self, event):
        raise NotImplementedError

    def Show(self):
        self.parent.SetTitle(self.title)
        super().Show()
