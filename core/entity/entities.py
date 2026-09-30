from random import random
import random
from core.gamelayer import GameObject

for_render = []
states = ["fresh", "crackled", "destroyed"]
types = ["hardened", "softened", "crackled"]


class Entity(GameObject):
    def __init__(self, image, pos, dimensions=(1, 1)):
        super().__init__(image, pos, dimensions)
        for_render.append(self)

    def pos(self):
        return self.pos
    def set_pos(self, pos):
        self.pos = pos
    def move(self, displacement):
        self.pos[0] += displacement[0]
        self.pos[1] += displacement[1]

class Ship(Entity):
    def __init__(self, pos=(1, 0)):
        super().__init__("ship.png", pos)

        self.state = states[random.randint(0, 2)]
        self.type = types[random.randint(0, 2)]
        self.hardness = random.randint(1, 10)

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
    def state(self):
        return self.state


SHIP = Ship()
ROCK = Rock()
WALL = Wall()
PRESS = Press()


def get_for_render() -> list[GameObject]:
    return for_render