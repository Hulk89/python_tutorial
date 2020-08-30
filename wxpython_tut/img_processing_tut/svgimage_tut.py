import io

import wx 
from wx.svg import SVGimage

import drawSvg as draw
import hyperbolic.poincare.shapes as hyper  # pip3 install hyperbolic

class SVG():
    """points를 받아서 svg image를 그리고 bytes로 반환하는 객체"""
    def __init__(self):
        """반지름이 1인 원을 생성하고, group하나를 만든다."""
        self.image_size = 500
        self.d = draw.Drawing(2, 2, origin='center')  # viewbox(-1, -1, 2, 2)
        self.d.setRenderSize(self.image_size)
        self.d.append(draw.Circle(0, 0, 1, fill='orange'))

        group = draw.Group()
        self.d.append(group)

    def draw(self, points):
        """points를 받아, 그림을 그린다."""
        group = self.d.elements[-1] ##GG
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
    @property
    def image_bytes(self):
        image_buffer = io.StringIO()
        self.d.asSvg(outputFile=image_buffer)
        image_buffer.seek(0)
        return str.encode(image_buffer.getvalue())


class MyFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY, "svg test")
        self.svg = SVG()
        self.points = []
        self.svg.draw(self.points)
        self.img = SVGimage.CreateFromBytes(self.svg.image_bytes)

        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_MOTION, self.on_move)
        self.Bind(wx.EVT_PAINT, self.on_paint)
    
    def on_paint(self, event):
        self.img = SVGimage.CreateFromBytes(self.svg.image_bytes)
        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush('white'))
        dc.Clear()

        width = int(self.img.width * self.scale)
        height = int(self.img.height * self.scale)

        ctx = wx.GraphicsContext.Create(dc)
        self.img.RenderToGC(ctx, self.scale)

    @property
    def scale(self):
        dcdim = min(self.ClientSize.width, self.ClientSize.height)
        imgdim = min(self.img.width, self.img.height)
        scale = dcdim / imgdim
        return scale

    @staticmethod
    def frame_to_svg_coord(frame_pos, scale, image_size):
        x, y = frame_pos
        # 좌상단이 0, 0에서 center가 0, 0이며, y축이 반대가 됨
        pos = (x / scale - image_size/2, image_size/2 - y / scale)
        # scale 변환(svg안에서 실제 coord는 -1~1임)
        pos = tuple(p / (image_size / 2) for p in pos)
        return pos

    def on_move(self, event):
        pos = self.frame_to_svg_coord(event.GetPosition(),
                                      self.scale,
                                      self.svg.image_size)
        self.svg.draw(self.points + [pos])
        self.Refresh()

    def on_left_down(self, event):
        pos = self.frame_to_svg_coord(event.GetPosition(),
                                      self.scale,
                                      self.svg.image_size)
        self.points.append(pos)
        self.svg.draw(self.points)
        self.Refresh()


app = wx.App(False) # A Frame is a top-level window.
frame = MyFrame(None)
frame.Show(True)
#import wx.lib.inspection
#wx.lib.inspection.InspectionTool().Show()
app.MainLoop()
