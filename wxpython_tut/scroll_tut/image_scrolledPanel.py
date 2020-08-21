from glob import glob

import wx
import wx.lib.scrolledpanel as scrolled

class ImageScrollPanel(scrolled.ScrolledPanel):
    def __init__(self, parent, files, width):
        scrolled.ScrolledPanel.__init__(self, parent, -1)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        for _file in files:
            img = wx.Image(_file, wx.BITMAP_TYPE_ANY)
            height = int(img.GetHeight() / img.GetWidth() * width)

            img = img.Scale(width, height)
            bitmap = wx.StaticBitmap(self,
                                     wx.ID_ANY,
                                     bitmap=img.ConvertToBitmap())
            bSizer.Add(bitmap, 0, wx.ALL | wx.EXPAND, 0)
        
        self.SetSizer(bSizer)
        self.SetupScrolling()


class EpisodeFrame(wx.Frame):
    def __init__(self, parent, title, files, width=800):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                          title=title,
                          pos=wx.DefaultPosition,
                          size=wx.DefaultSize,
                          style=wx.DEFAULT_FRAME_STYLE)

        _ = ImageScrollPanel(self, files, width)

        self.SetSize(wx.Size(width, 600))

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

if __name__ == '__main__':
    files = sorted(glob('testimg/*.png'))
    app = wx.App()
    frame = EpisodeFrame(None, 'Image viewer with scrolledpanel', files)
    frame.Show(True)
    app.MainLoop()


