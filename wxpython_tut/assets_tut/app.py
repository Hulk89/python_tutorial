import wx # Create a new app, don't redirect stdout/stderr to a window.

import os
import sys
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':
    app = wx.App(False) # A Frame is a top-level window.
    
    frame = wx.Frame(None, wx.ID_ANY, "Hello Python") # Show the frame.
    frame.Show(True)

    img = wx.Image(resource_path('assets/save.png'), wx.BITMAP_TYPE_PNG)
    bmp = wx.StaticBitmap(parent=frame, bitmap=img.ConvertToBitmap())
    app.MainLoop()
