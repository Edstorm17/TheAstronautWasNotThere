import pygame

import config
from game.entity import entities
from config import TILE_SIZE

SCREEN = None
scroll_x = 0
scroll_y = 0

def init(screen):
    global SCREEN
    global scroll_x
    global scroll_y

    SCREEN = screen
    scroll_x = screen.get_width()//2 - config.map_size*TILE_SIZE//2
    scroll_y = screen.get_height()//2 - config.map_size*TILE_SIZE//2

def draw_background(screen):
    screen.fill("darkorchid4")

def draw_game_layer(screen):
    def draw_obj_gl(img, pos, dimensions):
        x = pos[0]*TILE_SIZE + scroll_x
        y = pos[1]*TILE_SIZE + scroll_y

        screen.blit(img, (x, y))

    def draw_ground(size):
        raw_image = pygame.image.load("assets/ground.png")
        ground_image = pygame.transform.scale(raw_image, (TILE_SIZE, TILE_SIZE))

        for row in range(size):
            for col in range(size):
                draw_obj_gl(ground_image, (col, row), (size, size))

    draw_ground(config.map_size)

    for entity in entities.get_for_render():
        draw_obj_gl(entity.image, entity.pos, entity.dimensions)

def draw_all():
    draw_background(SCREEN)
    draw_game_layer(SCREEN)