import wx
import os

class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(
            self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        bSizer1.Add(self.m_staticText3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_dirPicker2 = wx.DirPickerCtrl(
            self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        bSizer1.Add(self.m_dirPicker2, 1, wx.ALL | wx.EXPAND, 5)

        m_choice1Choices = []
        self.m_choice1 = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        bSizer1.Add(self.m_choice1, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.m_dirPicker2.Bind(wx.EVT_DIRPICKER_CHANGED, self.on_dir_changed)
        self.m_choice1.Bind(wx.EVT_CHOICE, self.on_choice)

    def __del__(self):
        pass

    def on_dir_changed(self, event):
        path = event.GetPath()
        dirs = [d for d in os.listdir(path)]
        self.m_choice1.SetItems(dirs)
        self.set_label()
    def on_choice(self, event):
        event.Skip()
        self.set_label()

    def set_label(self):
        selection = self.m_choice1.GetSelection()
        label = self.m_choice1.GetString(selection)
        self.m_staticText3.SetLabel(label)


    
app = wx.App(False)
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
