import io

import wx 
from wx.svg import SVGimage

import drawSvg as draw
import hyperbolic.poincare.shapes as hyper  # pip3 install hyperbolic

class SVG():
    def __init__(self, points):
        # Create drawing
        self.d = draw.Drawing(2, 2, origin='center')
        self.d.setRenderSize(500)
        self.d.append(draw.Circle(0, 0, 1, fill='orange'))
        group = draw.Group()
        self.d.append(group)

        self.points = points

    def draw(self):
        group = self.d.elements[-1] ##GG
        points = self.points
        group.children.clear()
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
        self.svg = SVG([(0.1, 0.1), (0.5,0.5)])
        self.svg.draw()
        image_buffer = io.StringIO()
        self.svg.d.asSvg(outputFile=image_buffer)
        image_buffer.seek(0)
        self.img = SVGimage.CreateFromBytes(
                str.encode(image_buffer.getvalue()))
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush('white'))
        dc.Clear()

        dcdim = min(self.Size.width, self.Size.height)
        imgdim = min(self.img.width, self.img.height)
        scale = dcdim / imgdim
        width = int(self.img.width * scale)
        height = int(self.img.height * scale)

        ctx = wx.GraphicsContext.Create(dc)
        self.img.RenderToGC(ctx, scale)


app = wx.App(False) # A Frame is a top-level window.
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
