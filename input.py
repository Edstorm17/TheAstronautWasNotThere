import config
import renderer
from core.entity.entities import Entity
from core.entity import entities
import pygame
from core.item import items
from core.games.game1 import e

arrow_down_counter_y = 0
arrow_down_counter_x = 0

# button : left click=1, middle click=2, right click=3, wheelup=4, wheeldown=5

class Mouse:
    def __init__(self):
        self.buttons_down = [False]*3
        self.displacement = (0, 0)
        self.mousewheel = (0, 0)

    def button_down(self, pos, button, touch):
        match button:
            case 1 | 2 | 3:
                self.buttons_down[button-1] = True
            case 4:
                renderer.zoom(1, pos)
            case 5:
                renderer.zoom(-1, pos)

    def button_up(self, pos, button, touch):
        if button <= 3:
            self.buttons_down[button-1] = False

    def motion(self, pos, rel, buttons, touch):
        self.displacement = rel

        if buttons[0]:
            renderer.scroll(rel)

class Keyboard:
    def __init__(self):
        self.keys_down = {}

    def key_down(self, key, mod, unicode, scancode):
        self.keys_down[key] = True

        global arrow_down_counter_y
        global arrow_down_counter_x
        if key == pygame.K_UP:#up
            entities.SHIP.move((0, 1))


        if key == pygame.K_RIGHT:# right arrow

            entities.SHIP.move((1, 0))

        if key == pygame.K_LEFT: #left arrow

            entities.SHIP.move((-1, 0))


        if key == pygame.K_DOWN:#down arrow
            entities.SHIP.move((0, -1))

        if key == pygame.K_SPACE:
            if entities.SHIP.get_pos() in e:
                e.pop(entities.SHIP.get_pos()).delete()
                items.gold.increment()
            else:
                print("no rock")

    def key_up(self, key, mod, unicode, scancode):
        self.keys_down[key] = False

    def get_key_state(self, key):
        return self.keys_down.get(key, False)

mouse = Mouse()
keyboard = Keyboard()