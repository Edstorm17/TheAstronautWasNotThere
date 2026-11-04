import pygame
import pygame_gui
import ui.gui

from ui.element import ElementWrapper


class TreeWindow(ElementWrapper):
    def __init__(self, manager):
        ele = pygame_gui.elements.UIWindow(rect=pygame.Rect(0, 0, 800, 600), manager=manager.manager, window_display_title="Upgrades", always_on_top=True)
        self.clicked_on = False
        super().__init__(ele, {
            pygame_gui.UI_WINDOW_CLOSE: self.on_window_close,
            pygame.MOUSEMOTION: lambda e: ele.rect.collidepoint(pygame.mouse.get_pos()) | self.clicked_on,
            pygame.MOUSEBUTTONDOWN: self.on_click,
            pygame.MOUSEBUTTONUP: self.on_up
        }, manager)

    def on_click(self, event):
        self.clicked_on = True
        return False

    def on_up(self, event):
        self.clicked_on = False
        return False

    def on_window_close(self, event) -> bool:
        ui.gui.reset_manager()
        return True