import pygame
import pygame_gui
from pygame import draw

import renderer

focused = None
text = ""
lines = [""]
box_x = 50
box_y = 50
box_width = 700
line_height = 35
windows: list[CodeWindow] = []
color_index = {
    "def": (252,90,3),}

class ElementWrapper:
    def __init__(self, element_internal, event_funcs: dict):
        self.element_internal = element_internal
        self.event_funcs = event_funcs
        from gui.gui import register_events
        register_events(self)

class CodeWindow(ElementWrapper):
    def __init__(self, manager):
        from gui.gui import update_scaling_elements, moving_elements
        def click_func():
            if not self.focused:
                self.focused = True
            print("focused or not ")

        def keydown_func():
           if self.focused:
               pass
        self.text = []
        self.manager = manager
        self.text = ""
        self.cursor_position = 0
        self.focused = False
        print(windows)
        self.jhg = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 20), (box_width, 50)), manager=self.manager)
        self.jhg.show()
        super().__init__(self.jhg ,{})
        windows.append(self)
        print(windows)

        # Button(relative_rect=pygame.Rect((0, 0), (50, 25)), text="play", object_id="play", manager=manager,container=jhg)
        # Button(relative_rect=pygame.Rect((50, 0), (50, 25)), text="move", object_id="move", manager=manager,container=jhg)
        # Button(relative_rect=pygame.Rect((100, 0), (50, 25)), text="scale", object_id="scale", manager=manager,container=jhg, click_func=lambda e: update_scaling_elements(jhg))
        moving_elements.append((self.jhg, (300 - renderer.scroll_x, 100 - renderer.scroll_y), (260, 70)))

def draw_text():
    #for i in range()
    text_box = pygame_gui.elements.UITextBox(
        html_text= focused.text,
        relative_rect= pygame.Rect((0, 0), (560, 360)),
        manager= focused.manager,
        container= focused.jhg)


def set_focused(pos):
    global focused
    for window in windows:
        if window.element_internal.rect.collidepoint(pos):
            focused = window
            return



def key_down(event):
    if focused is not None:
        if event.key == pygame.K_BACKSPACE:
            print("packspace")
            remove = ""

            focused.text = focused.text[:-1:]

        else:
            focused.text = focused.text + str(event.unicode)
        draw_text()
        print(focused.text)


class Button(ElementWrapper):
    def __init__(self, relative_rect, text, object_id, manager, click_func, container=None):
        button = pygame_gui.elements.UIButton(relative_rect=relative_rect, text=text, object_id=object_id, manager=manager, container=container)
        button.show()
        super().__init__(button, {pygame_gui.UI_BUTTON_PRESSED: click_func})
