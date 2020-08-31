import os
import wx  # Create a new app, don't redirect stdout/stderr to a window.


class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_dirPicker1 = wx.DirPickerCtrl(
            self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        bSizer1.Add(self.m_dirPicker1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl1 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        bSizer1.Add(self.m_textCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.m_dirPicker1.Bind(wx.EVT_DIRPICKER_CHANGED, self.on_dir_picker_changed)

    def __del__(self):
        pass

    def on_dir_picker_changed(self, event):
        dir_path = event.GetPath()
        self.m_textCtrl1.Clear()
        self.m_textCtrl1.AppendText(dir_path)

app = wx.App(False)
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
