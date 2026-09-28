import renderer


# button : left click=1, middle click=2, right click=3, wheelup=4, wheeldown=5

class Mouse:
    def __init__(self):
        self.buttons_down = [False]*3
        self.displacement = (0, 0)
        self.mousewheel = (0, 0)

    def button_down(self, event):
        match event.button:
            case 1 | 2 | 3:
                self.buttons_down[event.button-1] = True
            case 4:
                renderer.zoom(1, event.pos)
            case 5:
                renderer.zoom(-1, event.pos)

    def button_up(self, event):
        if event.button <= 3:
            self.buttons_down[event.button-1] = False

    def motion(self, event):
        self.displacement = event.rel

        if event.buttons[0]:
            renderer.scroll(event.rel)

    def wheel(self, event):
        self.mousewheel = (event.x, event.y)

mouse = Mouse()
