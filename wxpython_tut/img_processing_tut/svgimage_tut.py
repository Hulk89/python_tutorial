import io

import wx 
from wx.svg import SVGimage

import drawSvg as draw
import hyperbolic.poincare.shapes as hyper  # pip3 install hyperbolic

class SVG():
    def __init__(self):
        # Create drawing
        self.image_size = 500
        self.d = draw.Drawing(2, 2, origin='center')
        self.d.setRenderSize(self.image_size)
        #self.d.append(draw.Circle(0, 0, 1, fill='orange'))
        image = draw.Image(-1, -1, 2, 2, path='./image.png')

        self.d.append(image)

        group = draw.Group()
        self.d.append(group)

    def draw(self, points):
        group = self.d.elements[-1] ##GG
        group.children.clear()
        points = [(p[0] / (self.image_size / 2),
                   p[1] / (self.image_size / 2)) for p in points]

        for x1, y1 in points:
            for x2, y2 in points:
                if (x1, y1) == (x2, y2): continue
                p1 = hyper.Point.fromEuclid(x1, y1)
                p2 = hyper.Point.fromEuclid(x2, y2)
                if p1.distanceTo(p2) <= 2:
                    line = hyper.Line.fromPoints(*p1, *p2, segment=True)
                    group.draw(line, hwidth=0.2, fill='white')
        for x, y in points:
            p = hyper.Point.fromEuclid(x, y)
            group.draw(hyper.Circle.fromCenterRadius(p, 0.1),
                    fill='green')


class MyFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY, "svg test")
        self.svg = SVG()
        self.points = []
        self.svg.draw(self.points)
        self.refresh_img()

        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_MOTION, self.on_move)
        self.Bind(wx.EVT_PAINT, self.on_paint)
    
    def refresh_img(self):
        image_buffer = io.StringIO()
        self.svg.d.asSvg(outputFile=image_buffer)
        image_buffer.seek(0)

        self.img = SVGimage.CreateFromBytes(
                str.encode(image_buffer.getvalue()))

    def on_paint(self, event):
        self.refresh_img()
        dc = wx.PaintDC(self)
        #dc.SetBackground(wx.Brush('white'))
        dc.Clear()

        width = int(self.img.width * self.scale)
        height = int(self.img.height * self.scale)

        ctx = wx.GraphicsContext.Create(dc)
        self.img.RenderToGC(ctx, self.scale)

    @property
    def scale(self):
        dcdim = min(self.Size.width, self.Size.height)
        imgdim = min(self.img.width, self.img.height)
        scale = dcdim / imgdim
        return scale

    def on_move(self, event):
        x, y = event.GetPosition()
        ## TODO: position validation check
        ## TODO: position to svg points
        pos = (x / self.scale - self.svg.image_size/2,
                self.svg.image_size/2 - y / self.scale)
        self.svg.draw(self.points + [pos])
        self.Refresh()
        

    def on_left_down(self, event):
        x, y = event.GetPosition()
        pos = (x / self.scale - self.svg.image_size/2,
               self.svg.image_size/2 - y / self.scale)
        self.points.append(pos)
        self.svg.draw(self.points)
        self.Refresh()
        


app = wx.App(False) # A Frame is a top-level window.
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
