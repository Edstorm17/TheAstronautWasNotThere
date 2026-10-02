import pygame
import pygame_gui

from ui.code_window import CodeWindow

moving_elements = []
registered_events = {}

def on_add_button_pressed(event, manager):
   CodeWindow(event,manager)

class Button:
    def __init__(self, relative_rect, text, object_id, manager, func=None,container= None):
        self.button = pygame_gui.elements.UIButton(relative_rect=relative_rect,text=text,object_id=object_id,manager=manager,container=container,)
        self.func = func
        register_event(pygame_gui.UI_BUTTON_PRESSED, self)
        if object_id == "scale":
            register_event(pygame_gui.UI_BUTTON_START_PRESS, self)

def init(ui_manager):
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

def update_moving_elements(scroll, scale=None):
    for e, p, s in moving_elements:
        e.set_position((p[0]+scroll[0], p[1]+scroll[1]))
        if scale:
            e.set_dimensions((s[0]*scale, s[1]*scale))
            for child in e.get_container().elements:
                child.set_dimensions((s[0]*scale, s[1]*scale), clamp_to_container=False)

def is_mouse_over_element():
    mouse_pos = pygame.mouse.get_pos()
    for e, _, _ in moving_elements:
        if e.rect.collidepoint(mouse_pos):
            return True
    return False

def update_scaling_elements(self,container):
    while pygame.MOUSEBUTTONDOWN:
        if register_event(pygame.MOUSEMOTION, ):
            pygame.transform.scale()