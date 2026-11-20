import logging
import time
from typing import Callable, Any

from core.entity import entities
from core.games.game1 import map as rocks
from core.item import items
import re
global colors
from ui.colors import Colors

register_match = re.compile(r"%\w+")

process_delay = 0.5

class CodeException(Exception):
    pass

class Argument:
    def __init__(self, *arg_type: re.Pattern | str | type[int] | type[str]):
        self.type = arg_type

    def value(self, ctx: CodeProcessor, lit: str):
        for t in self.type:
            if t is int:
                if lit.isdigit():
                    return int(lit)
            elif isinstance(t, re.Pattern):
                if t.fullmatch(lit):
                    return ctx.registers[lit]
            elif isinstance(t, str):
                if lit == t:
                    return lit
            elif t is str:
                return lit
        raise CodeException(f"Invalid argument {lit}.")

registered_methods: dict[str, Method] = {}

class Method:
    def __init__(self, name: str, function: Callable, *arg_types: Argument):
        self.name: str = name
        self.func: Callable = function
        self.arg_types = arg_types
        registered_methods[name] = self
        Colors("add",self.name,"#FFA500")

    def call(self, context: CodeProcessor, args: list[str]):
        if len(args) != len(self.arg_types):
            raise CodeException(f"Invalid argument length for {self.name} : Expected {len(self.arg_types)} arguments, but got instead {len(args)}.")
        args = [ty.value(context, arg) for arg, ty in zip(args, self.arg_types)]
        return self.func(context, *args)

INT_VAR_ARG = Argument(register_match, int)
STR_VAR_ARG = Argument(register_match, str)
VAR_ARG = Argument(register_match, int, str)

def move_func(ctx, direction: str, steps: int):
    directions = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    max_steps = 100

    if steps > max_steps:
        raise CodeException(ctx.index, f"too fat steps {steps}, max {max_steps}")

    if steps > ctx.move_counter:
        entities.SHIP.move(directions[direction])
        ctx.move_counter += 1
        if ctx.move_counter >= steps:
            ctx.move_counter = 0
        else:
            ctx.index -= 1

def harv_func(ctx):
    if entities.SHIP.get_pos() in rocks:
        rocks.pop(entities.SHIP.get_pos()).delete()
        items.argon.increment()

def jump_func(ctx, target: int, condition: int):
    if condition:
        ctx.index = target - 1

def put_func(ctx, value: str | int, register: str):
    if not register_match.fullmatch(register):
        raise CodeException(f"Invalid register {register}.")

    ctx.registers[register] = value
    print(ctx.registers)

Method("mv", move_func, Argument("up", "right", "down", "left"), INT_VAR_ARG)
Method("harv", harv_func)
Method("jump", jump_func, INT_VAR_ARG, INT_VAR_ARG)
Method("put", put_func, VAR_ARG, Argument(str))

class CodeProcessor:
    def __init__(self):
        self._code_lines = []
        self.index = 0
        self.last_call = time.time() - process_delay
        self.logger = logging.getLogger(__name__)

        self.registers = {}

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
        if not op in registered_methods:
            self.logger.warning(f"{self.index} Invalid operation {op}.")
        try:
            registered_methods[op].call(self, args)
        except CodeException as e:
            self.logger.warning(e)
        #     case 'put':
        #         if len(args) != 2:
        #             self.logger.warning(self.index, "put prend deux arguments (valeur, destination)")
        #             return False
        #         if not args[0].isdigit():
        #             self.logger.warning(self.index, "seul les nombres sont acceptés dans les registers")
        #             return False
        #         if not bool(register_match.fullmatch(args[1])):
        #             self.logger.warning(self.index, "le nom du register est invalide")
        #
        #         self.registers[args[1]] = int(args[0])
        #         print(self.registers)
        #     case _:
        #         self.logger.log(self.index, f"c quoi ca??? :  '{op}'")
        #         return False

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