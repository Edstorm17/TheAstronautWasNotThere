import pygame
import pygame_gui
import ui.gui

from ui.element import ElementWrapper


class TreeWindow(ElementWrapper):
    def __init__(self, manager):
        ele = pygame_gui.elements.UIWindow(rect=pygame.Rect(0, 0, 800, 600), manager=manager.manager, window_display_title="Upgrades", always_on_top=True)
        super().__init__(ele, {
            pygame_gui.UI_WINDOW_CLOSE: self.on_window_close
        }, manager)

    def on_window_close(self, event) -> bool:
        ui.gui.reset_manager()
        return True