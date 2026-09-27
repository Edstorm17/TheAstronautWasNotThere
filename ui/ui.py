import pygame
import pygame_gui

registered_events = {}

def init(manager):
    add_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)), text="+", manager=manager)
    def on_add_button_pressed(event):
        print("add_button_pressed")
    register_event(pygame_gui.UI_BUTTON_PRESSED, on_add_button_pressed)

def register_event(event_id, func):
    if registered_events.get(event_id) is None:
        registered_events[event_id] = [func]
    else:
        registered_events[event_id].append(func)

def handle_event(event):
    if event.type in registered_events:
        for func in registered_events[event.type]:
            func(event)