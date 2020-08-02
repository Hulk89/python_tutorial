import wx

import os
import sys
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':
    app = wx.App(False) # A Frame is a top-level window.
    
    if hasattr(sys, '_MEIPASS'):
        title = "app has path: {}".format(sys._MEIPASS)
    else:
        title = "Hello Python"
    frame = wx.Frame(None, wx.ID_ANY, title) # Show the frame.
    frame.Show(True)

    img = wx.Image(resource_path('assets/save.png'), wx.BITMAP_TYPE_PNG)
    bmp = wx.StaticBitmap(parent=frame, bitmap=img.ConvertToBitmap())

    app.MainLoop()
