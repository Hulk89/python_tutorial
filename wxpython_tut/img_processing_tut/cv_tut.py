import io

import wx 
import cv2

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

class Canvas(wx.Panel):
    def __init__(self, parent, image_filepath):
        super().__init__(parent, wx.ID_ANY)
        self.set_image(image_filepath)

        self.m_bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panel = wx.Panel(self, wx.ID_ANY, style=wx.TRANSPARENT_WINDOW)

        self.draw(self.points)

        self.panel.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.panel.Bind(wx.EVT_MOTION, self.on_move)
        self.Bind(wx.EVT_SIZE, self.on_resize)

    def set_image(self, image_filepath):
        self.image_filepath = image_filepath
        self.points = []
        img = cv2.imread(self.image_filepath)
        h, w, *_ = img.shape
        self.image_size = (w, h)

    def draw(self, points):
        image = cv2.imread(self.image_filepath)

        for chunk in chunks(points, 4):
            if len(chunk) == 4:
                chunk += [chunk[0]]
            for i in range(len(chunk) - 1):
                cv2.line(image, chunk[i], chunk[i+1], (255, 0, 0), 3)

        is_success, img_buffer = cv2.imencode(".jpg", image)
        io_buf = io.BytesIO(img_buffer)

        # convert to wx.Image and set bitmap
        # TODO: 이미지가 세로로 길면 세로로 꽉 맞게 만들기
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
            w, h = self.image_size
            scale = w / bitmap_width
            self.points.append((int(scale * x), int(scale * y)))

        self.draw(self.points)

    def on_move(self, event):
        x, y = event.GetPosition()

        bitmap_width, bitmap_height = self.m_bitmap.Size
        frame_height = self.Size.height

        if y < bitmap_height:
            w, h = self.image_size
            scale = w / bitmap_width
            self.draw(self.points + [(int(scale * x), int(scale * y))])

    def on_resize(self, event):
        self.draw(self.points)



class MyFrame(wx.Frame):
    def __init__(self, parent, image):
        super().__init__(parent, wx.ID_ANY, "opencv box test")
        bSizer = wx.BoxSizer(wx.VERTICAL)

        text = wx.StaticText(self, wx.ID_ANY, "opencv box test")
        bSizer.Add(text, 0, wx.ALL| wx.EXPAND, 5)

        canvas = Canvas(self, image)
        canvas.SetBackgroundColour("blue")
        bSizer.Add(canvas, 1, wx.ALL | wx.EXPAND, 5)
        
        button = wx.Button(self, wx.ID_ANY, "button")
        button.SetBackgroundColour("red")
        bSizer.Add(button, 0, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(bSizer)
        self.Layout()

app = wx.App(False) # A Frame is a top-level window.
frame = MyFrame(None, 'image.png')
frame.Show(True)
app.MainLoop()
