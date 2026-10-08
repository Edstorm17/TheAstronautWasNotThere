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
    "def": (252,90,3),

}

class ElementWrapper:
    def __init__(self, element_internal, event_funcs: dict, manager):
        self.element_internal = element_internal
        self.event_funcs = event_funcs
        self.manager = manager
        self.event_funcs = event_funcs
        manager.register_events(self)

class CodeWindow(ElementWrapper):
    def __init__(self, manager):
        self.text = []
        self.text = ""
        self.cursor_position = 0
        self.focused = False
        print(windows)
        self.jhg = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 20), (box_width, 50)), manager=manager.manager)
        self.jhg.show()
        super().__init__(self.jhg ,{
            pygame.MOUSEBUTTONDOWN: self.on_click,
            pygame.KEYDOWN: self.on_key_down
        }, manager)
        windows.append(self)
        print(windows)

        # Button(relative_rect=pygame.Rect((0, 0), (50, 25)), text="play", object_id="play", manager=manager,container=jhg)
        # Button(relative_rect=pygame.Rect((50, 0), (50, 25)), text="move", object_id="move", manager=manager,container=jhg)
        # Button(relative_rect=pygame.Rect((100, 0), (50, 25)), text="scale", object_id="scale", manager=manager,container=jhg, click_func=lambda e: update_scaling_elements(jhg))
        manager.moving_elements.append((self.jhg, (300 - renderer.scroll_x, 100 - renderer.scroll_y), (260, 70)))

    def on_click(self, event):
        if not is_mouse_over(self):
            return
        self.focused = True
        global focused
        focused = self
        print("focused or not ")

    def on_key_down(self, event):
        global focused
        if focused == self:
            print(event.unicode)
            if event.key == pygame.K_BACKSPACE:
                focused.text = focused.text[:-1]
            elif event.key == 13:
                print("entred")
                focused.text += "line.\n"
            else:
                focused.text += event.unicode
                print(focused.text)

def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)

def draw_text():
    from ui.gui import GameGUIManager
    if focused is not None and isinstance(focused.manager, GameGUIManager):
        mot = ""
        for i in range(len(focused.text)):
            p = focused.text
            n = p[i]
            if n != " ":
                mot.join(n)
            else:
                for m in color_index.keys():
                    print("mot caché")
                    print(m)
                    if mot == m:

                        pass
                mot = ""



        text_box = pygame_gui.elements.UITextBox(
            html_text= focused.text,
            relative_rect= pygame.Rect((0, 0), (560, 360)),
            manager= focused.manager.manager,
            container= focused.jhg)


def set_focused(pos):
    global focused
    for window in windows:
        if window.element_internal.rect.collidepoint(pos):
            focused = window
            return





class Button(ElementWrapper):
    def __init__(self, relative_rect, text, object_id, manager, click_func, container=None):
        button = pygame_gui.elements.UIButton(relative_rect=relative_rect, text=text, object_id=object_id, manager=manager.manager, container=container)
        button.show()
        super().__init__(button, {pygame_gui.UI_BUTTON_PRESSED: click_func}, manager)


def is_mouse_over(element: ElementWrapper):
    return element.element_internal.rect.collidepoint(pygame.mouse.get_pos())