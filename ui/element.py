from pydoc import html
import re
from pydoc import html
from typing import Callable

import pygame
import pygame_gui
from pygame.event import Event

import renderer
from games import code_processor

focused = None
text = ""
lines = [""]
box_x = 50
box_y = 50
timer = 0

line_height = 85
windows = []


class ElementWrapper:
    def __init__(self, element_internal, event_funcs: dict[int, Callable[[Event], bool]], manager):
        self.element_internal = element_internal
        self.event_funcs = event_funcs
        self.manager = manager
        manager.register_events(self)

class CodeWindow(ElementWrapper):
    """This code makes codes windows to allow player to code in game. This class work with a Manager set by the ElementWrapper"""
    def __init__(self, manager):
        self.lenght = {"0":0,}
        self.space = 0
        self.width = 170
        self.height = 70
        self.text = ""
        self.cursor_position = 0
        self.focused = False
        self.line_n = 0
        self.container = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 20), (self.width, self.height + 100*self.line_n)), manager=manager.manager)
        self.move = Button(relative_rect=pygame.Rect((50, 0), (50, 25)), text="move", object_id="move", manager=manager, container=self.container, click_func=None)
        self.moving = False

        super().__init__(self.container ,{
            pygame.MOUSEBUTTONDOWN: self.on_click,
            pygame.MOUSEBUTTONUP: self.on_up,
            pygame.KEYDOWN: self.on_key_down,
            pygame.MOUSEMOTION: self.on_motion
        }, manager)
        windows.append(self)

        Button(relative_rect=pygame.Rect((0, 0), (50, 25)), text="play", object_id="play", manager=manager, container=self.container, click_func=self.test)
        Button(relative_rect=pygame.Rect((100, 0), (50, 25)), text="scale", object_id="scale", manager=manager, container=self.container, click_func=self.test)
        manager.moving_elements.append((self.container, (300 - renderer.scroll_x, 100 - renderer.scroll_y), (260, 70)))

    def test(self, e) -> bool:

        text = getattr(self, "text", None)
        source = text.replace("\\n", "\n")

        processor = code_processor.new_processor()
        ls = source.splitlines()

        for raw in ls:
            line = raw.split(";")[0].split("#")[0].strip().lower()
            if not line:
                return True
            tokens = line.replace(",", " ").split()
            op, args = tokens[0], tokens[1:]
            processor.append_line((op, args))

        return True

    def on_motion(self, event) -> bool:
        if self.moving:
            x = self.element_internal.rect.x
            y = self.element_internal.rect.y
            self.element_internal.set_position((x + event.rel[0], y + event.rel[1]))
            return True

        return self.element_internal.rect.collidepoint(pygame.mouse.get_pos())

    def on_up(self, event) -> bool:
        self.moving = False
        return False

    def on_click(self, event) -> bool:
        global focused
        if not is_mouse_over(self):
            return False
        if self.move.element_internal.rect.collidepoint(pygame.mouse.get_pos()):
            self.moving = True
        self.focused = True
        focused = self
        return False

    def on_key_down(self, event) -> bool:
        """C'est le moyen de mettre le text entré par l'utilisateur dans la text box
        \n il handle
        - les backspace
        - les touches enter
        - toutes les lettres et nombres
        """
        global max
        global focused
        if focused == self:
            if event.key == pygame.K_BACKSPACE:
                if focused.text[-1:] == "\n":
                    focused.text = focused.text[0:-1]
                    focused.line_n -= 1
                    print("remove line ")
                else:
                    focused.text = focused.text[:-1]
                    print("remove thing")
                if focused.lenght[f"{focused.line_n}"] > 0:
                    focused.lenght[f"{focused.line_n}"] -= 4

            # la clé enter est pris en compte pour faire une nouvelle ligne
            elif event.key == 13:
                focused.text += "\n"
                focused.line_n += 1
                focused.lenght[f"{focused.line_n}"] = 0
            else:
                if event.key not in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]:

                    focused.text += event.unicode
                    focused.lenght[f"{focused.line_n}"] += 4

            max = 0
            for i in range(len(focused.lenght)):
                if focused.lenght[f"{max}"] < focused.lenght[f"{i}"]:
                    max = i
            focused.container.set_dimensions((focused.width + focused.lenght[f"{max}"] ,focused.height + 24 * focused.line_n),clamp_to_container=True)
            draw_text()
            return True


def draw_text():
    """C'est le renderer de texte qui va ajouter le code html au texte
    \n
    Il handle entre autre:
    - colorie les fonctions
    - colorie les noms de fonctions
    """
    global timer
    from ui.gui import GameGUIManager
    max = 0
    for i in range(len(focused.lenght)):
        if focused.lenght[f"{max}"] < focused.lenght[f"{i}"]:
            max = i
    if focused is not None and isinstance(focused.manager, GameGUIManager):
        p = html.escape(focused.text)
        p = re.sub(r'def\b', '<font color="#FFA500">def</font>', p)
        p = re.sub(r'(\w+)(?=\()', r'<font color="#004cff">\1</font>',p)
        p = p.replace("\n", "<br>")

        text_box = pygame_gui.elements.UITextBox(
            html_text= p,
            relative_rect= pygame.Rect((0, 25), ((300+focused.lenght[f"{max}"]), (360 + 24*focused.line_n))),
            manager= focused.manager.manager,
            container= focused.container)

class Button(ElementWrapper):
    def __init__(self, relative_rect, text, object_id, manager, click_func=lambda e: False, container=None):
        button = pygame_gui.elements.UIButton(relative_rect=relative_rect, text=text, object_id=object_id, manager=manager.manager, container=container)
        button.show()
        # if click_func is not None:
        super().__init__(button, {pygame_gui.UI_BUTTON_PRESSED: click_func}, manager)


def is_mouse_over(element: ElementWrapper):
    return element.element_internal.rect.collidepoint(pygame.mouse.get_pos())