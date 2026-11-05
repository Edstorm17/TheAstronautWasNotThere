from pydoc import html
from typing import Callable
from pygame.event import Event
import pygame
import pygame_gui
import re
import renderer
focused = None
text = ""
lines = [""]
box_x = 50
box_y = 50
timer = 0

line_height = 85
windows: list[CodeWindow] = []


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
        self.jhg = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 20), (self.width, self.height + 100*self.line_n)), manager=manager.manager)
        self.move = Button(relative_rect=pygame.Rect((50, 0), (50, 25)), text="move", object_id="move", manager=manager, container=self.jhg, click_func=None)
        self.moving = False

        super().__init__(self.jhg ,{
            pygame.MOUSEBUTTONDOWN: self.on_click,
            pygame.MOUSEBUTTONUP: self.on_up,
            pygame.KEYDOWN: self.on_key_down,
            pygame.MOUSEMOTION: self.on_motion
        }, manager)
        windows.append(self)

        Button(relative_rect=pygame.Rect((0, 0), (50, 25)), text="play", object_id="play", manager=manager, container=self.jhg, click_func=self.test)
        Button(relative_rect=pygame.Rect((100, 0), (50, 25)), text="scale", object_id="scale", manager=manager, container=self.jhg, click_func=None)
        manager.moving_elements.append((self.jhg, (300 - renderer.scroll_x, 100 - renderer.scroll_y), (260, 70)))

    def test(self, e):
        print("Clicked!")
        return False

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
            focused = None
            return False
        if self.move.element_internal.rect.collidepoint(pygame.mouse.get_pos()):
            self.moving = True
        self.focused = True
        focused = self
        return False

    def on_key_down(self, event) -> bool:
        global max
        global focused
        if focused == self:
            print(event.unicode)
            if event.key == pygame.K_BACKSPACE:
                if focused.text[-1:] == "\n":
                    focused.text = focused.text[0:-1]
                    focused.line_n -= 1
                    print("remove line ")
                else:
                    focused.text = focused.text[:-1]
                    print("remove thing")
                if focused.lenght[f"{focused.line_n}"] > 0:
                    focused.lenght[f"{focused.line_n}"] -= 3

            elif event.key == 13:
                print("entred")
                print(focused.text[-1:])
                if focused.text[-1::] == ":":
                    print("deux points!")
                    focused.text += "\n"
                    focused.text += "    "

                else:
                    print("normal")
                    focused.text += "\n"
                focused.line_n += 1
                focused.lenght[f"{focused.line_n}"] = 0
            else:
                focused.text += event.unicode
                focused.lenght[f"{focused.line_n}"] += 3
                print(focused.text)

        max = 0
        for i in range(len(focused.lenght)):
            if focused.lenght[f"{max}"] < focused.lenght[f"{i}"]:
                max = i
        focused.jhg.set_dimensions((focused.width + focused.lenght[f"{max}"] ,focused.height + 24 * focused.line_n),clamp_to_container=True)
        draw_text()
        return True

def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)

def draw_text():
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
            container= focused.jhg)


def set_focused(pos):
    global focused
    for window in windows:
        if window.element_internal.rect.collidepoint(pos):
            focused = window
        else:
            focused = None
            return





class Button(ElementWrapper):
    def __init__(self, relative_rect, text, object_id, manager, click_func=lambda e: False, container=None):
        button = pygame_gui.elements.UIButton(relative_rect=relative_rect, text=text, object_id=object_id, manager=manager.manager, container=container)
        button.show()
        # if click_func is not None:
        super().__init__(button, {pygame_gui.UI_BUTTON_PRESSED: click_func}, manager)


def is_mouse_over(element: ElementWrapper):
    return element.element_internal.rect.collidepoint(pygame.mouse.get_pos())