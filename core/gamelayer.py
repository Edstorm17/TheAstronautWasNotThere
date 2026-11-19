import pygame
from pygame.sprite import Sprite
from core.math_utils import Vec2
import config


class GameObject(Sprite):
    def __init__(self, image, pos: Vec2, dimensions : Vec2):
        super().__init__()


        self.dimensions = dimensions
        self.pos: Vec2  = pos

        raw_img = pygame.image.load(f"./assets/world_assets/{image}")
        self.image = pygame.transform.scale(raw_img, (config.TILE_SIZE * dimensions.x, config.TILE_SIZE*dimensions.y))
        self.rect = self.image.get_rect()

    def get_pos(self) -> Vec2:
        return self.pos

    def set_pos(self, pos):
        self.pos = pos

