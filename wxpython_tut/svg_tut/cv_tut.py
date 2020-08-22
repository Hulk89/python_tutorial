import io
from functools import lru_cache

import wx 
import cv2

@lru_cache(maxsize=16)
def imread(filepath):
    return cv2.imread(filepath)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

class MyFrame(wx.Frame):
    def __init__(self, parent, image):
        super().__init__(parent, wx.ID_ANY, "svg test")
        self.points = []
        self.image = image
        
        self.m_bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panel = wx.Panel(self, wx.ID_ANY, style=wx.TRANSPARENT_WINDOW)

        self.draw(self.points)

        self.panel.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.panel.Bind(wx.EVT_MOTION, self.on_move)  # TODO: staticbitmap motion bug, 투명한 panel
        self.Bind(wx.EVT_SIZE, self.on_resize)

    def draw(self, points):
        #image = imread(self.image).copy()
        image = cv2.imread(self.image)

        for chunk in chunks(points, 4):
            if len(chunk) == 4:
                chunk += [chunk[0]]
            for i in range(len(chunk) - 1):
                cv2.line(image, chunk[i], chunk[i+1], (255, 0, 0), 3)

        is_success, img_buffer = cv2.imencode(".jpg", image)
        io_buf = io.BytesIO(img_buffer)

        img = wx.Image(io_buf, mimetype='image/jpeg')
        width = self.Size.width
        height = int(img.GetHeight() / img.GetWidth() * width)
        img = img.Scale(width, height)

        self.m_bitmap.SetBitmap(img.ConvertToBitmap())
        self.panel.SetSize(self.m_bitmap.Size)

    def on_left_down(self, event):
        x, y = event.GetPosition()

        bitmap_width, bitmap_height = self.m_bitmap.Size
        frame_height = self.Size.height

        if y < bitmap_height:
            image = imread(self.image)
            h, w, *_ = image.shape
            scale = w / bitmap_width

            self.points.append((int(scale * x), int(scale * y)))

        self.draw(self.points)

    def on_move(self, event):
        x, y = event.GetPosition()

        bitmap_width, bitmap_height = self.m_bitmap.Size
        frame_height = self.Size.height

        if y < bitmap_height:
            image = imread(self.image)
            h, w, *_ = image.shape
            scale = w / bitmap_width
            self.draw(self.points + [(int(scale * x), int(scale * y))])

    def on_resize(self, event):
        self.draw(self.points)


app = wx.App(False) # A Frame is a top-level window.
frame = MyFrame(None, 'image.png')
frame.Show(True)
app.MainLoop()
