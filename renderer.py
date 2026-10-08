import pygame

import config
from ui import ui
from core.entity import entities
from config import TILE_SIZE
from core.item import items

SCREEN = None
map_px_size = config.map_size*TILE_SIZE
world_surface = pygame.Surface((map_px_size, map_px_size))
scroll_x = 0
scroll_y = 0
zoom_factor = 1
font = None

def init(screen):
    global SCREEN
    global scroll_x
    global scroll_y
    global font

    SCREEN = screen
    scroll_x = screen.get_width()//2 - map_px_size//2
    scroll_y = screen.get_height()//2 - map_px_size//2
    font = pygame.font.SysFont(None, 50)

def scroll(delta):
    global scroll_x
    global scroll_y
    scroll_x += delta[0]
    scroll_y += delta[1]
    ui.update_moving_elements((scroll_x, scroll_y))

def zoom(amount, zoom_center):
    global zoom_factor
    global scroll_x
    global scroll_y
    new_zoom_factor = zoom_factor * 1.1**amount
    scroll_x = zoom_center[0] - ((zoom_center[0]-scroll_x)/zoom_factor)*new_zoom_factor
    scroll_y = zoom_center[1] - ((zoom_center[1]-scroll_y)/zoom_factor)*new_zoom_factor
    zoom_factor = new_zoom_factor
    ui.update_moving_elements((scroll_x, scroll_y), scale=zoom_factor)

def draw_background(screen):
    screen.fill("darkorchid4")

def draw_game_layer(screen):
    def draw_text(text):
        for tex, color, start_pos, end_pos in text:
            surface = font.render(
                tex,
                True,
                color
            )

    def draw_obj_gl(img, pos, dimensions):
        rect = img.get_rect()

        x = pos[0]*TILE_SIZE
        y = screen.get_height()-pos[1]*TILE_SIZE
        rect.bottomleft = (x, y)

        screen.blit(img, rect)

    def draw_ground(size):
        raw_image = pygame.image.load("assets/world_assets/ground.png")
        ground_image = pygame.transform.scale(raw_image, (TILE_SIZE, TILE_SIZE))

        for row in range(size):
            for col in range(size):
                draw_obj_gl(ground_image, (col, row), (size, size))

    draw_ground(config.map_size)

    for entity in entities.get_for_render():
        draw_obj_gl(entity.image, entity.get_pos(), entity.dimensions)

def draw_ui_layer(screen):
    def draw_item(index, item):
        x = screen.get_width() - (index+1)*config.ITEM_SIZE
        screen.blit(item.image, (x, 0))
        text_surf = font.render(str(item.get_amount()), True, (255, 255, 255))
        text_rect = text_surf.get_rect()
        text_rect.center = (x+config.ITEM_SIZE//2, config.ITEM_SIZE)
        screen.blit(text_surf, text_rect)

    for i, tem in enumerate(items.get_for_render()):
        draw_item(i, tem)

def draw_all():
    draw_background(SCREEN)

    draw_game_layer(world_surface)

    map_scaled_size = int(map_px_size * zoom_factor)
    scaled_world_surface = pygame.transform.scale(world_surface, (map_scaled_size, map_scaled_size))

    SCREEN.blit(scaled_world_surface, (scroll_x, scroll_y))
    draw_ui_layer(SCREEN)
