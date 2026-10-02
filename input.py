import renderer
from core.entity import entities
from ui import ui

arrow_down_counter_y = 0
arrow_down_counter_x = 0

# button : left click=1, middle click=2, right click=3, wheelup=4, wheeldown=5
scroll_allowed = False

class Mouse:
    def __init__(self):
        self.buttons_down = [False]*3
        self.displacement = (0, 0)
        self.mousewheel = (0, 0)

    def button_down(self, pos, button, touch):
        match button:
            case 1:
                self.buttons_down[button-1] = True
                if not ui.is_mouse_over_element():
                    global scroll_allowed
                    scroll_allowed = True
            case 2 | 3:
                self.buttons_down[button-1] = True
            case 4:
                if not ui.is_mouse_over_element():
                    renderer.zoom(1, pos)
            case 5:
                if not ui.is_mouse_over_element():
                    renderer.zoom(-1, pos)

    def button_up(self, pos, button, touch):
        if button <= 3:
            self.buttons_down[button-1] = False
        if button == 1:
            global scroll_allowed
            scroll_allowed = False

    def motion(self, pos, rel, buttons, touch):
        self.displacement = rel

        if buttons[0] and scroll_allowed:
            renderer.scroll(rel)

class Keyboard:
    def __init__(self):
        self.keys_down = {}

    def key_down(self, key, mod, unicode, scancode):
        self.keys_down[key] = True

        global arrow_down_counter_y
        global arrow_down_counter_x
        global focused
        if key == 1073741906:#up
            # if arrow_down_counter_y > config.map_size:
            #     entities.BOMB.set_pos((arrow_down_counter_x, config.map_size))
            # arrow_down_counter_y += 1
            # entities.BOMB.set_pos((arrow_down_counter_x, arrow_down_counter_y))
            entities.BOMB.move((0, 1))


        elif key == 1073741903:# right arrow
            # if arrow_down_counter_x > 10:
            #     entities.BOMB.set_pos((10, arrow_down_counter_y))
            # arrow_down_counter_x += 1
            # entities.BOMB.set_pos((arrow_down_counter_x, arrow_down_counter_y))
            entities.BOMB.move((1, 0))

        elif key == 1073741904:#left arrow
            # if arrow_down_counter_x < 0:
            #     entities.BOMB.set_pos((0, arrow_down_counter_y))
            #
            # arrow_down_counter_x -= 1
            # entities.BOMB.set_pos((arrow_down_counter_x, arrow_down_counter_y))
            entities.BOMB.move((-1, 0))

            ...
        elif key == 1073741905:#down arrow
            # if arrow_down_counter_y < 0:
            #     entities.BOMB.set_pos((arrow_down_counter_x, 0))
            # arrow_down_counter_y -= 1
            # entities.BOMB.set_pos((arrow_down_counter_x, arrow_down_counter_y))
            entities.BOMB.move((0, -1))

        else:
            pass






    def key_up(self, key, mod, unicode, scancode):
        self.keys_down[key] = False

    def get_key_state(self, key):
        return self.keys_down.get(key, False)

mouse = Mouse()
keyboard = Keyboard()
