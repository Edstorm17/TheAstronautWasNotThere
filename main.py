import pygame
import pygame_gui

import config
import renderer
from ui import ui

pygame.init()
pygame.display.set_caption(config.TITLE)

screen = pygame.display.set_mode(config.WINDOW_SIZE)
clock = pygame.time.Clock()
ui_manager = pygame_gui.UIManager(config.WINDOW_SIZE)

renderer.init(screen)
ui.init(ui_manager)

running = True

while running:
    time_delta = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        ui.handle_event(event)

        ui_manager.process_events(event)

    ui_manager.update(time_delta)

    renderer.draw_all()
    ui_manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()