import pygame
import pygame_gui

import renderer

focused = False
text = ""
lines = [""]
box_x = 50
box_y = 50
box_width = 700
line_height = 35
windows: list[CodeWindow] = []

class ElementWrapper:
    def __init__(self, element_internal, event_funcs: dict):
        self.element_internal = element_internal
        self.event_funcs = event_funcs
        from ui.ui import register_events
        register_events(self)

class CodeWindow(ElementWrapper):
    def __init__(self, keydown_func, manager):
        from ui.ui import update_scaling_elements,moving_elements
        global focused

        self.manager = manager
        self.text = ""
        self.cursor_position = 0
        self.focused = False
        print(windows)
        jhg = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 20), (box_width, 50)), manager=self.manager)
        jhg.show()
        super().__init__(jhg ,{pygame.KEYDOWN: keydown_func})
        windows.append(self)
        print(windows)

        # Button(relative_rect=pygame.Rect((0, 0), (50, 25)), text="play", object_id="play", manager=manager,container=jhg)
        # Button(relative_rect=pygame.Rect((50, 0), (50, 25)), text="move", object_id="move", manager=manager,container=jhg)
        # Button(relative_rect=pygame.Rect((100, 0), (50, 25)), text="scale", object_id="scale", manager=manager,container=jhg, click_func=lambda e: update_scaling_elements(jhg))
        moving_elements.append((jhg, (300 - renderer.scroll_x, 100 - renderer.scroll_y), (260, 70)))


class Button(ElementWrapper):
    def __init__(self, relative_rect, text, object_id, manager, click_func, container=None):
        button = pygame_gui.elements.UIButton(relative_rect=relative_rect, text=text, object_id=object_id, manager=manager, container=container)
        button.show()
        super().__init__(button, {pygame_gui.UI_BUTTON_PRESSED: click_func})
