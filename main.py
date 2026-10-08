import pygame
import pygame_gui
from core.games.game1 import new_level
import config
import input
import renderer
from ui import ui

pygame.init()
pygame.display.set_caption(config.TITLE)

screen = pygame.display.set_mode(config.WINDOW_SIZE)
clock = pygame.time.Clock()
ui_manager = pygame_gui.UIManager(config.WINDOW_SIZE, theme_path="assets/ui_assets/theme.json")

renderer.init(screen)
ui.init(ui_manager)

running = True

new_level(10)

while running:
    time_delta = clock.tick(60)/1000
    for event in pygame.event.get():
        if not (ui.handle_event(event) or ui_manager.process_events(event)):

            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.MOUSEBUTTONDOWN:
                    input.mouse.button_down(event.pos, event.button, event.touch)
                case pygame.MOUSEBUTTONUP:
                    input.mouse.button_up(event.pos, event.button, event.touch)
                case pygame.MOUSEMOTION:
                    input.mouse.motion(event.pos, event.rel, event.buttons, event.touch)
                case pygame.KEYDOWN:
                    input.keyboard.key_down(event.key, event.mod, event.unicode, event.scancode)
                case pygame.KEYUP:
                    input.keyboard.key_up(event.key, event.mod, event.unicode, event.scancode)

    ui_manager.update(time_delta)

    renderer.draw_all()
    ui_manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()