import pygame
from pygame.sprite import Sprite

import config


class GameObject(Sprite):
    def __init__(self, image, pos, dimensions):
        super().__init__()


        self.dimensions = dimensions
        self.x = pos[0]
        self.y = pos[1]

        raw_img = pygame.image.load(f"assets/world_assets/{image}")
        self.image = pygame.transform.scale(raw_img, (config.TILE_SIZE*dimensions[0], config.TILE_SIZE*dimensions[1]))
        self.rect = self.image.get_rect()

    def get_pos(self):
        return self.x, self.y

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

