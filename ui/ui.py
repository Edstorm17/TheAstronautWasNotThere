import pygame
import pygame_gui

from ui.element import ElementWrapper

moving_elements = []
registered_events: dict[int, list[ElementWrapper]] = {}

def on_add_button_pressed(event, manager):
    from ui.element import CodeWindow
    CodeWindow(manager)


def init(ui_manager):
    from ui.element import Button
    Button(relative_rect=pygame.Rect((0, 0), (50, 50)), text="", object_id="#add_button", manager=ui_manager, click_func=lambda event: on_add_button_pressed(event, ui_manager))
    # Button(relative_rect=pygame.Rect((0, 100), (50, 50)), text="test \n button", object_id="#test2button", manager=ui_manager)

def register_events(element: ElementWrapper):
    for k in element.event_funcs.keys():
        register_event(k, element)

def register_event(event_id, element: ElementWrapper):
    if registered_events.get(event_id) is None:
        registered_events[event_id] = [element]
    else:
        registered_events[event_id].append(element)

def handle_event(event):
    from ui.element import set_focused, focused
    if event.type == pygame.KEYDOWN:
        print(focused)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        set_focused(event.pos)
    if event.type in registered_events:
        for ele in registered_events[event.type]:
            if event.ui_element == ele.element_internal:
                ele.event_funcs[event.type](event)
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
        pass


    print("focused")