import pygame
import pygame_gui

from ui.element import ElementWrapper


class TreeWindow(ElementWrapper):
    def __init__(self, manager):
        ele = pygame_gui.elements.UIWindow(rect=pygame.Rect(0, 0, 800, 600), manager=manager.manager, window_display_title="Upgrades", always_on_top=True)
        super().__init__(ele, {

        }, manager)
