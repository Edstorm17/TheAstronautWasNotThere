import logging
import time

from core.entity import entities
from core.games.game1 import e as rocks
from core.item import items

process_delay = 0.5

class CodeProcessor:
    def __init__(self):
        self._code_lines = []
        self.index = 0
        self.last_call = time.time() - process_delay
        self.logger = logging.getLogger(__name__)

        self.move_counter = 0
        
    def append_line(self, line: tuple[str, list[str]]):
        self._code_lines.append(line)
        
    def append_lines(self, lines: list[tuple[str, list[str]]]):
        for line in lines:
            self.append_line(line)
            
    def set_index(self, idx):
        self.index = idx
            
    def process_next_line(self):
        if len(self._code_lines) > self.index and self.last_call + process_delay <= time.time():
            self.process(self._code_lines[self.index][0], self._code_lines[self.index][1])
            self.index += 1
            self.last_call += process_delay
        elif len(self._code_lines) <= self.index:
            global active_processor
            active_processor = None
            del self
            
    def process(self, op, args):
        print(op, args)
        match op:
            case 'mv':
                directions = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
                max_steps = 100
                
                if len(args) != 2:
                    self.logger.log(self.index, "mv a besoin de deux arguments (direction, int)")
                    return False
                direction = args[0]
                if direction not in directions:
                    self.logger.log(self.index, f"mauvaise dirs '{direction}'")
                    return False
                if not args[1].isdigit():
                    self.logger.log(self.index, f"le deuxième argument doit être un nombre entier")
                    return False
                steps = int(args[1])
                if steps > max_steps:
                    self.logger.log(self.index, f"too fat steps {steps}, max {max_steps}")
                    return False

                if steps > self.move_counter:
                    entities.SHIP.move(directions[direction])
                    self.move_counter += 1
                    if self.move_counter >= steps:
                        self.move_counter = 0
                    else:
                        self.index -= 1
            case 'harv':
                if len(args) != 0:
                    self.logger.log(self.index, "harv a besoin d'aucun arguments")
                    return False

                if entities.SHIP.get_pos() in rocks:
                    rocks.pop(entities.SHIP.get_pos()).delete()
                    items.argon.increment()
            case 'jump':
                if len(args) != 1:
                    self.logger.log(self.index, "jump a besoin d'un seul argument")
                    return False
                if not args[0].isdigit():
                    self.logger.log(self.index, "le premier argument doit être un nombre entier")
                    return False

                target = int(args[0])

                self.index = target - 2
            case _:
                self.logger.log(self.index, f"c quoi ca??? :  '{op}'")
                return False

        return True
            
active_processor: CodeProcessor | None = None

def new_processor():
    global active_processor
    active_processor = CodeProcessor()
    return active_processor

def process_next_if_available():
    if active_processor:
        active_processor.process_next_line()
        return True
    return False