import logging
import time
from typing import Callable, Any

from core.entity import entities
from core.games import game1
import re
global colors
from ui.colors import Colors

register_match = re.compile(r"%\w+")
return_value_register = "%ret"

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
    def __init__(self, name: str, function: Callable, *arg_types: Argument, delay=0.0):
        self.name: str = name
        self.func: Callable = function
        self.arg_types = arg_types
        self.delay = delay
        registered_methods[name] = self
        Colors("add",fr"\W*({self.name})\W*","#FFA500")

    def call(self, ctx: CodeProcessor, args: list[str]):
        if len(args) != len(self.arg_types):
            raise CodeException(f"Invalid argument length for {self.name} : Expected {len(self.arg_types)} arguments, but got instead {len(args)}.")
        args = [ty.value(ctx, arg) for arg, ty in zip(args, self.arg_types)]
        ret = self.func(ctx, *args)
        ctx.set_delay(self.delay)
        return ret

INT_VAR_ARG = Argument(register_match, int)
STR_VAR_ARG = Argument(register_match, str)
VAR_ARG = Argument(register_match, int, str)
STR_ARG = Argument(str)

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
    game1.harvest()

def jump_func(ctx, target: int, condition: int):
    if condition:
        ctx.index = target - 1

def put_func(ctx, value: str | int, register: str):
    if not register_match.fullmatch(register):
        raise CodeException(f"InvaFixlid register {register}.")

    ctx.registers[register] = value
    print(ctx.registers)

def get_pos_x(ctx):
    return entities.SHIP.get_pos().x

def get_pos_y(ctx):
    return entities.SHIP.get_pos().y

def equals(ctx, value1: int | str, value2: int | str):
    return value1 == value2

def smaller(ctx, value1: int, value2: int):
    return value1 < value2

def smaller_equals(ctx, value1: int, value2: int):
    return value1 <= value2

def greater(ctx, value1: int, value2: int):
    return value1 > value2

def greater_equals(ctx, value1: int, value2: int):
    return value1 >= value2

def add(ctx, value: int, register: str):
    if not register_match.fullmatch(register):
        raise CodeException(f"Invalid register {register}.")

    if register not in ctx.registers:
        raise CodeException(f"Register {register} is not initialised.")
    if not isinstance(ctx.registers[register], int):
        raise CodeException(f"Invalid register value {register}.")
    ctx.registers[register] += value

def sub(ctx, value: int, register: str):
    if not register_match.fullmatch(register):
        raise CodeException(f"Invalid register {register}.")

    if register not in ctx.registers:
        raise CodeException(f"Register {register} is not initialised.")
    if not isinstance(ctx.registers[register], int):
        raise CodeException(f"Invalid register value {register}.")
    ctx.registers[register] -= value

def div(ctx, value: int, register: str):
    if not register_match.fullmatch(register):
        raise CodeException(f"Invalid register {register}.")

    if register not in ctx.registers:
        raise CodeException(f"Register {register} is not initialised.")
    if not isinstance(ctx.registers[register], int):
        raise CodeException(f"Invalid register value {register}.")
    ctx.registers[register] /= value

def mul(ctx, value: int, register: str):
    if not register_match.fullmatch(register):
        raise CodeException(f"Invalid register {register}.")

    if register not in ctx.registers:
        raise CodeException(f"Register {register} is not initialised.")
    if not isinstance(ctx.registers[register], int):
        raise CodeException(f"Invalid register value {register}.")
    ctx.registers[register] *= value

def andd(ctx, value1: int, value2: int):
    return int(value1 and value2)

def nott(ctx, value: int):
    return int(not value)

def orr(ctx, value1: int, value2: int):
    return int(value1 or value2)

Method("mv", move_func, Argument("up", "right", "down", "left"), INT_VAR_ARG, delay=0.2)
Method("harv", harv_func, delay=0.2)
Method("jump", jump_func, INT_VAR_ARG, INT_VAR_ARG)
Method("put", put_func, VAR_ARG, STR_ARG)
Method("posx", get_pos_x)
Method("posy", get_pos_y)
Method("eq", equals, VAR_ARG, VAR_ARG)
Method("sm", smaller, INT_VAR_ARG, INT_VAR_ARG)
Method("gr", greater, INT_VAR_ARG, INT_VAR_ARG)
Method("sme", smaller_equals, INT_VAR_ARG, INT_VAR_ARG)
Method("gre", greater_equals, INT_VAR_ARG, INT_VAR_ARG)
Method("add", add, INT_VAR_ARG, STR_ARG)
Method("sub", sub, INT_VAR_ARG, STR_ARG)
Method("div", div, INT_VAR_ARG, STR_ARG)
Method("mul", mul, INT_VAR_ARG, STR_ARG)
Method("and", andd, INT_VAR_ARG, INT_VAR_ARG)
Method("not", nott, INT_VAR_ARG)
Method("or", orr, INT_VAR_ARG, INT_VAR_ARG)

class CodeProcessor:
    def __init__(self):
        self._code_lines = []
        self.index = 0
        self.next_call = time.time()
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

    def set_delay(self, seconds):
        self.next_call = time.time() + seconds

    def process_next_line(self):
        if len(self._code_lines) > self.index and self.next_call <= time.time():
            self.process(self._code_lines[self.index][0], self._code_lines[self.index][1])
            self.index += 1
            # self.last_call += process_delay
        elif len(self._code_lines) <= self.index:
            global active_processor
            active_processor = None
            del self
            
    def process(self, op, args):
        print(op, args)
        if not op in registered_methods:
            self.logger.warning(f"{self.index} Invalid operation {op}.")
        try:
            ret = registered_methods[op].call(self, args)
            self.registers[return_value_register] = ret
        except CodeException as e:
            self.logger.warning(e)

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