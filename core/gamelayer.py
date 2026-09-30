import pygame
from pygame.sprite import Sprite

import config


class GameObject(Sprite):
    def __init__(self, image, pos, dimensions):
        super().__init__()


        self.dimensions = dimensions
        self.pos = pos

        raw_img = pygame.image.load(f"assets/{image}")
        self.image = pygame.transform.scale(raw_img, (config.TILE_SIZE*dimensions[0], config.TILE_SIZE*dimensions[1]))
        self.rect = self.image.get_rect()

class ObjectAttributes(GameObject):
    def __init__(self, seed, difficulty):
        self.state = ...
        self.difficulty = difficulty
        self.type = ...
    def get_attributes(self,state, difficulty, seed):
        object().__init__()







