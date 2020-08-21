import wx
import gui

class MainApp(gui.MainFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.panels = [Panel1(self)]
    def Show(self, *args, **kwargs):
        super().Show(*args, **kwargs)
        self.panels[-1].Show()

class Panel1(gui.PanelWithButton):
    def __init__(self, parent, prev_title=""):
        super().__init__(parent, prev_title + ' > Panel1')
        self.parent = parent
        self.b_button.Disable()

    def forward(self, event):
        if self.IsShown():
            # hide panel1
            self.Hide()
            # make panel2 and show it
            panel = Panel2(self.parent, self.title)
            self.parent.panels.append(panel)
            panel.Show()


class Panel2(gui.PanelWithButton):
    def __init__(self, parent, prev_title=""):
        super().__init__(parent, prev_title + ' > Panel2')
        self.parent = parent

    def backward(self, event):
        # pop
        self.parent.panels.pop()
        # return to panelOne
        self.parent.panels[-1].Show()
        # destroy itself
        self.Destroy()

    def forward(self, event):
        if self.IsShown():
            self.Hide()
            panel = Panel3(self.parent, self.title)
            self.parent.panels.append(panel)
            panel.Show()


class Panel3(gui.PanelWithButton):
    def __init__(self, parent, prev_title=""):
        super().__init__(parent, prev_title + ' > Panel3')
        self.parent = parent
        self.f_button.Disable()

    def backward(self, event):
        # pop
        self.parent.panels.pop()
        # return to panelOne
        self.parent.panels[-1].Show()
        # destroy itself
        self.Destroy()


def main():
    app = wx.App()
    window = MainApp(None)
    window.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
