import pygame
from pygame.sprite import Sprite

import config


class GameObject(Sprite):
    def __init__(self, image, pos, dimensions):
        super().__init__()
        # self.surfaces = [Surface([width*SCALING_FACTOR, height*SCALING_FACTOR]) for _ in colors]
        # for i, surf in enumerate(self.surfaces):
        #     surf.fill(colors[i])
        #
        # self.spread = 10

        self.dimensions = dimensions
        self.pos = pos

        raw_img = pygame.image.load(f"assets/{image}")
        self.image = pygame.transform.scale(raw_img, (config.TILE_SIZE*dimensions[0], config.TILE_SIZE*dimensions[1]))
        self.rect = self.image.get_rect()

    # def draw(self, screen, pos):
    #     for i, surf in enumerate(self.surfaces):
    #         screen.blit(surf, (pos[0] - surf.get_width() // 2, pos[1] - surf.get_height() // 2 + i * self.spread))


# class Group3D(Group):
#     def __init__(self):
#         super().__init__()
#
#     def draw(self, surface, bgd = None, special_flags = 0):
#         for sprite in self.sprites():
#             if isinstance(sprite, Sprite3D):
#                 sprite.draw(surface, )
