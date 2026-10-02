import pygame
from pygame_gui.elements import UIPanel

#from main import screen
from ui.ui import *

focused = False
text = ""
lines = [""]
box_x = 50
box_y = 50
box_width = 700
line_height = 35
windows = list()


def focus_handler(event):
    for window in windows:
        if window[1].collidepoint(event.pos):
            window[0].focused = True


class CodeWindow:


    def __init__(self, event,manager):
        global focused

        self.manager = manager
        self.text = ""
        self.cursor_position = 0
        self.focused = False
        print(windows)

        windows.append((self,(pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((box_x, box_y), (box_width, 50 )), manager=self.manager ))))
        print(windows)
       # Button(relative_rect=pygame.Rect((0, 0), (50, 25)), text="play", object_id="play", manager=manager,container=jhg)
       # Button(relative_rect=pygame.Rect((50, 0), (50, 25)), text="move", object_id="move", manager=manager,container=jhg)
       # Button(relative_rect=pygame.Rect((100, 0), (50, 25)), text="scale", object_id="scale", manager=manager,container=jhg, func=lambda: update_scaling_elements(jhg))
        #moving_elements.append((jhg, (300 - renderer.scroll_x, 100 - renderer.scroll_y), (260, 70)))

    def keyboard_handler(self):
        pass
