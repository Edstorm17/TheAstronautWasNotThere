import pygame
import pygame_gui

import renderer

moving_elements = []
scaling_elements = []
registered_events = {}


def on_add_button_pressed(event, manager):
    jhg = pygame_gui.ui_manager.UIContainer(relative_rect=pygame.Rect((300,100), (260,70)), manager=manager, is_window_root_container=True)
    jhg.show()
    Button(relative_rect=pygame.Rect((0, 0), (50, 25)), text="play",object_id="play",manager=manager,container=jhg)
    pygame_gui.elements.UITextEntryBox(relative_rect=pygame.Rect((0, 20), (250, 50)), manager=manager, container=jhg).show()
    moving_elements.append((jhg, (300-renderer.scroll_x, 100-renderer.scroll_y)))

class Button:
    def __init__(self, relative_rect, text, object_id, manager, func=None,container= None):
        self.button = pygame_gui.elements.UIButton(relative_rect=relative_rect,text=text,object_id=object_id,manager=manager,container=container)
        self.func = func
        register_event(pygame_gui.UI_BUTTON_PRESSED, self)
        if object_id == "play":
            register_event(pygame_gui.UI_BUTTON_ON_HOVERED, self)

def init(ui_manager, win_manager):
    Button(relative_rect=pygame.Rect((0, 0), (50, 50)), text="", object_id="#add_button", manager=ui_manager, func=lambda event: on_add_button_pressed(event, ui_manager))
    Button(relative_rect=pygame.Rect((0, 100), (50, 50)), text="test \n button", object_id="#test2button", manager=ui_manager)


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

def update_moving_elements(scroll):
    for e, p in moving_elements:
        e.set_position((p[0]+scroll[0], p[1]+scroll[1]))

def update_scaling_elements(scroll):
    for e, p in moving_elements:
        pass