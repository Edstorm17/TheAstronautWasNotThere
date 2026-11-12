from random import random
import random
import config
from core.gamelayer import GameObject
from core.math_utils import Vec2
for_render = []
ships = []
states = ["fresh", "crackled", "destroyed"]
types = ["hardened", "softened", "crackled"]


class Entity(GameObject):
    def __init__(self, image, pos, dimensions: Vec2 = Vec2(1, 1), auto_render=True):
        super().__init__(image, pos, dimensions)
        if auto_render:
            for_render.append(self)

    def move(self, displacement: Vec2):
        self.pos = (self.pos+displacement).max(0).min(config.map_size-1)
    def delete(self):
        if self in for_render:
            for_render.remove(self)




class Ship(Entity):
    def __init__(self, pos : Vec2):
        super().__init__("ship.png", pos)
        self.name = "ship"

        self.state = states[random.randint(0, 2)]
        self.type = types[random.randint(0, 2)]
        self.hardness = random.randint(1, 10)
        ships.append(self)
#rocks have 3 states: fresh, crackled, destroyed
#the player can get the rock position and type, the type deetermines the hardness of the rock
class Argon(Entity):
    def __init__(self, pos: Vec2):
        super().__init__("argon_item.png", pos)
        self.name = "rock"
        self.state = states[random.randint(0,2)]
        self.type = types[random.randint(0, 2)]
        self.hardness = random.randint(1, 10)
class Gold(Entity):
        def __init__(self, pos: Vec2):
            super().__init__("gold_item.png", pos)
            self.name = "gold"

            self.state = states[random.randint(0, 2)]
            self.type = types[random.randint(0, 2)]
            self.hardness = random.randint(1, 10)


class Wall(Entity):
    def __init__(self, pos : Vec2):
        super().__init__("wall.png", pos)
        self.name = "wall"

        self.state = states[random.randint(0,2)]
        self.type = types[random.randint(0, 2)]
        self.hardness = random.randint(1, 10)

class Press(Entity):
    def __init__(self, pos: Vec2):
        super().__init__("press.png", pos)
        self.name = "press"
        self.compacting_power = 1
        self.state = states[random.randint(0, 2)]
class Drill(Entity):
    def __init__(self, pos: Vec2):
        super().__init__("drill.png", pos)
        self.name = "drill"
        self.state = states[random.randint(0, 2)]
        self.type = types[random.randint(0, 2)]
class Bomb(Entity):
    def __init__(self, pos: Vec2):
        super().__init__("bomb.png", pos)
        self.name = "bomb"
        self.state = states[random.randint(0, 2)]
        self.type = types[random.randint(0, 2)]
        self.hardness = random.randint(1, 10)
SHIP = Ship(Vec2())


def get_for_render() -> list[Entity]:
    return for_render