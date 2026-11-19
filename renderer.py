import pygame

import config
from ui import gui
from core.entity import entities
from config import TILE_SIZE
from core.item import items
import time
from core.math_utils import Vec2

SCREEN = None
map_px_size = config.map_size*TILE_SIZE
world_surface = pygame.Surface((map_px_size, map_px_size))
scroll_factor = Vec2()
zoom_factor = 1
font = None

def init(screen):
    global SCREEN, scroll_factor, font

    SCREEN = screen
    scroll_factor = Vec2(screen.get_width()//2, screen.get_height()//2) - map_px_size//2
    font = pygame.font.SysFont(None, 50)

def scroll(delta: Vec2):
    global scroll_factor
    scroll_factor += delta
    gui.update_moving_elements(scroll_factor)

def zoom(amount, zoom_center: Vec2):
    global zoom_factor, scroll_factor
    new_zoom_factor = min(max(zoom_factor * 1.1**amount, 0.5),3)
    scroll_factor = zoom_center - ((zoom_center-scroll_factor)/zoom_factor) * new_zoom_factor
    zoom_factor = new_zoom_factor
    gui.update_moving_elements(scroll_factor, scale=zoom_factor)
j = pygame.image.load('assets/ui_assets/background.png')
def draw_background(screen):
    screen.blit(j)

def draw_game_layer(screen):
    def draw_text(text):
        for tex, color, start_pos, end_pos in text:
            surface = font.render(
                tex,
                True,
                color
            )

    def draw_obj_gl(img, pos: Vec2, dimensions):
        rect = img.get_rect()
        rect.bottomleft = (pos.x * TILE_SIZE, screen.get_height()-pos.y*TILE_SIZE)

        screen.blit(img, rect)

    def draw_ground(size):
        raw_image = pygame.image.load("assets/world_assets/ground.png")
        ground_image = pygame.transform.scale(raw_image, (TILE_SIZE, TILE_SIZE))

        for row in range(size):
            for col in range(size):
                draw_obj_gl(ground_image, Vec2(col, row), Vec2(size, size))

    draw_ground(config.map_size)

    for entity in entities.get_for_render():
        draw_obj_gl(entity.image, entity.get_pos(), entity.dimensions)

    for ship in entities.ships:
        draw_obj_gl(ship.image, ship.get_pos(), ship.dimensions)

timeout_images = []

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

    for img, timeout_time in timeout_images:
        if time.time() > timeout_time:
            timeout_images.remove((img, timeout_time))
            continue

        screen.blit(img, img.get_rect())

def show(img, timeout):
    timeout_images.append((img, time.time() + timeout))
def win(g):
    SCREEN.blit(g)

def draw_all():
    draw_background(SCREEN)

    draw_game_layer(world_surface)

    map_scaled_size = int(map_px_size * zoom_factor)
    scaled_world_surface = pygame.transform.scale(world_surface, (map_scaled_size, map_scaled_size))

    SCREEN.blit(scaled_world_surface, tuple(scroll_factor))
    draw_ui_layer(SCREEN)


