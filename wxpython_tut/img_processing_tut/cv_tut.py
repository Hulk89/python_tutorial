import io

import wx 
import cv2

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

class Canvas(wx.Panel):
    def __init__(self, parent, image_filepath):
        super().__init__(parent, wx.ID_ANY)
        self.m_bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panel = wx.Panel(self, wx.ID_ANY, style=wx.TRANSPARENT_WINDOW)

        self.panel.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.panel.Bind(wx.EVT_MOTION, self.on_move)
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.set_image(image_filepath)

    def set_image(self, image_filepath):
        self.image_filepath = image_filepath
        self.points = []
        img = cv2.imread(self.image_filepath)
        h, w, *_ = img.shape
        self.image_size = (w, h)

        self.draw(self.points)

    def draw(self, points):
        # draw boxes 
        image = cv2.imread(self.image_filepath)

        for chunk in chunks(points, 4):
            if len(chunk) == 4:
                chunk += [chunk[0]]
            for i in range(len(chunk) - 1):
                cv2.line(image, chunk[i], chunk[i+1], (255, 0, 0), 3)
        _, img_buffer = cv2.imencode(".jpg", image)
        io_buf = io.BytesIO(img_buffer)

        # convert to wx.Image and set bitmap
        img = wx.Image(io_buf, mimetype='image/jpeg')

        img_ratio = self.image_size[0] / self.image_size[1]
        panel_ratio = self.Size.width / self.Size.height

        if img_ratio > panel_ratio:  # image의 width가 더 긴 경우
            width = self.Size.width
            height = int(img.GetHeight() / img.GetWidth() * width)
            pos = (0, (self.Size.height - height) // 2)
        else:
            height = self.Size.Height
            width = int(img.GetWidth() / img.GetHeight() * height)
            pos = ((self.Size.width - width) // 2, 0)

        img = img.Scale(width, height)
        self.m_bitmap.SetBitmap(img.ConvertToBitmap())
        self.m_bitmap.SetPosition(pos)
        self.panel.SetPosition(pos)
        self.panel.SetSize(self.m_bitmap.Size)

    def on_left_down(self, event):
        x, y = event.GetPosition()
        self.points.append(self.point_to_image_coord(x, y))
        self.draw(self.points)

    def on_move(self, event):
        x, y = event.GetPosition()
        self.draw(self.points + [self.point_to_image_coord(x, y)])

    def point_to_image_coord(self, x, y):
        """panel에서 얻은 좌표를 이미지 좌표계로 변환해준다.
        """
        bitmap_width, _ = self.m_bitmap.Size
        w, _ = self.image_size
        scale = w / bitmap_width

        return (int(scale * x), int(scale * y))

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
        
        button = wx.Button(self, wx.ID_ANY, "reset button")
        button.SetBackgroundColour("red")

        bSizer.Add(button, 0, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(bSizer)
        self.Layout()

        self.image = image
        self.canvas = canvas
        button.Bind(wx.EVT_BUTTON, self.reset_image)

    def reset_image(self, event):
        self.canvas.set_image(self.image)

app = wx.App(False) # A Frame is a top-level window.
frame = MyFrame(None, 'image.png')
frame.Show(True)
app.MainLoop()
