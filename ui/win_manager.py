import pygame
import pygame_gui

import renderer


class WinManager(pygame_gui.UIManager):
    def __init__(self, resolution, theme_path):
        super().__init__(resolution, theme_path)

    def draw_ui(self, window_surface: pygame.surface.Surface):
        scroll = (renderer.scroll_x, renderer.scroll_y)
        for visible in self.ui_group.visible:
            window_surface.blit(visible[0], (visible[1].x+scroll[0], visible[1].top+scroll[1]))