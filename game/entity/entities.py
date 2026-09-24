import pygame
from pygame.sprite import Sprite, Group


class Ship(Sprite):
    def __init__(self, x = 50, y = 50):
        super().__init__()

        self.image = pygame.image.load("assets/ship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

def get_group() -> Group:
    group = Group()
    group.add(Ship())
    return group