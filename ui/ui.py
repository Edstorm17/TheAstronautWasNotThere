import pygame
import pygame_gui
import threading

import renderer

registered_events = {}


def on_add_button_pressed(event,manager):
    scroll_x = renderer.scroll_x
    scroll_y = renderer.scroll_y
    pi = pygame_gui.elements
    jhg = pygame_gui.elements.UIWindow(rect=pygame.Rect((300, 100), (100, 100)), manager=manager,draggable=True,resizable=True,)
    hello_button = pygame_gui.elements.UITextEntryBox(relative_rect=pygame.Rect((scroll_x, scroll_y), (250, 50)),manager=jhg)



class Button:
    def __init__(self, relative_rect, text, object_id, manager, func=None):
        self.button = pygame_gui.elements.UIButton(relative_rect=relative_rect,text=text,object_id=object_id,manager=manager)
        self.func = func
        register_event(pygame_gui.UI_BUTTON_PRESSED, self)


def init(manager):
    Button(relative_rect=pygame.Rect((0, 0), (50, 50)), text="", object_id="#add_button", manager=manager, func=lambda event: on_add_button_pressed(event, manager))
    Button(relative_rect=pygame.Rect((0, 100), (100, 100)), text="", object_id="#test2button", manager=manager)


def register_event(event_id, but):
    if registered_events.get(event_id) is None:
        registered_events[event_id] = [but]
    else:
        registered_events[event_id].append(but)

def handle_event(event):
    if event.type in registered_events:
        for ele in registered_events[event.type]:
            if event.ui_element == ele.button:
                if ele.func:
                    ele.func(event)
        return True
    return False

