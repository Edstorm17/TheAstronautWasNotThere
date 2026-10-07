import pygame

from ui.element import ElementWrapper, CodeWindow, Button

class GUIManager:
    def __init__(self, ui_manager):
        self.manager = ui_manager
        self.registered_events: dict[int, list[ElementWrapper]] = {}

    def register_events(self, element: ElementWrapper):
        for k in element.event_funcs.keys():
            self.register_event(k, element)

    def register_event(self, event_id, element: ElementWrapper):
        if self.registered_events.get(event_id) is None:
            self.registered_events[event_id] = [element]
        else:
            self.registered_events[event_id].append(element)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.key_down(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_button_down(event)
        if event.type in self.registered_events:
            for ele in self.registered_events[event.type]:
                if event.ui_element == ele.element_internal:
                    ele.event_funcs[event.type](event)
            return True
        return False

    def key_down(self, event):
        pass

    def mouse_button_down(self, event):
        pass

class GameGUIManager(GUIManager):
    def __init__(self, ui_manager):
        super().__init__(ui_manager)
        self.moving_elements = []

        def on_add_button_pressed(self, event):
            CodeWindow(self.manager)

        Button(relative_rect=pygame.Rect((0, 0), (50, 50)), text="", object_id="#add_button", manager=self.manager, click_func=lambda event: on_add_button_pressed(event, self.manager))

    def update_moving_elements(self, scroll, scale=None):
        for e, p, s in self.moving_elements:
            e.set_position((p[0] + scroll[0], p[1] + scroll[1]))
            if scale:
                e.set_dimensions((s[0] * scale, s[1] * scale))
                for child in e.get_container().elements:
                    child.set_dimensions((s[0] * scale, s[1] * scale), clamp_to_container=False)

    def is_mouse_over_element(self):
        mouse_pos = pygame.mouse.get_pos()
        for e, _, _ in self.moving_elements:
            if e.rect.collidepoint(mouse_pos):
                return True
        return False


active_manager: GUIManager | None = None
game_gui_manager: GameGUIManager | None = None

def init(ui_manager):
    global game_gui_manager
    global active_manager
    game_gui_manager = GameGUIManager(ui_manager)

    active_manager = game_gui_manager

def current_manager():
    global active_manager
    return active_manager

def update_moving_elements(scroll, scale=None):
    if isinstance(active_manager, GameGUIManager):
        active_manager.update_moving_elements(scroll, scale)

def is_mouse_over_element(self):
    if isinstance(active_manager, GameGUIManager):
        mouse_pos = pygame.mouse.get_pos()
        for e, _, _ in self.moving_elements:
            if e.rect.collidepoint(mouse_pos):
                return True
        return False
    return False