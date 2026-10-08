from random import random
import random
import config
from core.gamelayer import GameObject

for_render = []
ships = []
states = ["fresh", "crackled", "destroyed"]
types = ["hardened", "softened", "crackled"]


class Entity(GameObject):
    def __init__(self, image, pos, dimensions=(1, 1), render_auto=True):
        super().__init__(image, pos, dimensions)
        if render_auto:
            for_render.append(self)

    def move(self, displacement):
        self.x = min(max(self.x + displacement[0], 0), config.map_size-1)
        self.y = min(max(self.y + displacement[1], 0), config.map_size-1)

class Ship(Entity):
    def __init__(self, pos=(1, 0)):
        super().__init__("ship.png", pos, render_auto=False)

        self.state = states[random.randint(0, 2)]
        self.type = types[random.randint(0, 2)]
        self.hardness = random.randint(1, 10)
        ships.append(self)
    def pos(self):
        return self.pos
    def state(self):
        return self.state
    def type(self):
        return self.type
    def hardness(self):
        return self.hardness

#rocks have 3 states: fresh, crackled, destroyed
#the player can get the rock position and type, the type deetermines the hardness of the rock
class Rock(Entity):
    def __init__(self, pos=(2, 0)):
        super().__init__("rock.png", pos)

        self.state = states[random.randint(0,2)]
        self.type = types[random.randint(0, 2)]
        self.hardness = random.randint(1, 10)
    def pos(self):
        return self.pos
    def state(self):
        return self.state
    def type(self):
        return self.type
    def hardness(self):
        return self.hardness

class Wall(Entity):
    def __init__(self, pos=(3, 0)):
        super().__init__("wall.png", pos)

        self.state = states[random.randint(0,2)]
        self.type = types[random.randint(0, 2)]
        self.hardness = random.randint(1, 10)
    def pos(self):
        return self.pos
    def state(self):
        return self.state
    def type(self):
        return self.type
    def hardness(self):
        return self.hardness

class Press(Entity):
    def __init__(self, pos=(4, 0)):
        super().__init__("press.png", pos)
        self.compacting_power = 1
        self.state = states[random.randint(0, 2)]
    def compact(self, state):
        return state + self.compacting_power
    def pos(self):
        return self.pos
    def state(self):
        return self.state
class Drill(Entity):
    def __init__(self, pos=(5, 0)):
        super().__init__("drill.png", pos)
        self.state = states[random.randint(0, 2)]
        self.type = types[random.randint(0, 2)]
class Bomb(Entity):
    def __init__(self, pos=(5, 1)):
        super().__init__("bomb.png", pos)
        self.state = states[random.randint(0, 2)]
        self.type = types[random.randint(0, 2)]
        self.hardness = random.randint(1, 10)
BOMB = Bomb()
SHIP = Ship()
ROCK = Rock()
WALL = Wall()
PRESS = Press()
DRILL = Drill()


def get_for_render() -> list[Entity]:
    return for_render