from random import random
import random
from core.gamelayer import GameObject

for_render = []

class Entity(GameObject):
    def __init__(self, image, pos, dimensions = (1, 1)):
        super().__init__(image, pos, dimensions)
        for_render.append(self)

    def set_pos(self, pos):
        self.pos = pos

    def move(self, displacement):
        self.pos[0] += displacement[0]
        self.pos[1] += displacement[1]

class Ship(Entity):
    def __init__(self, pos=(0, 0)):
        super().__init__("ship.png", pos)
    def get_level(self):
        ...

        # malik -> TreeUpgrade = get_ship_level()
        # return TreeUpgrade


class Rock(Entity):
    def __init__(self, pos=(0, 0)):
        super().__init__("rock.jpg", pos)

    def hardness(self):
        hardness = random.randint(1, 10)
        return hardness




class Wall(Entity):
    def __init__(self, pos=(0, 0)):
        super().__init__("wall.png", pos)

    def hardness(self):
        hardness = random.randint(1, 10)
        return hardness





SHIP = Ship()
ROCK = Rock()
WALL = Wall()


def get_for_render() -> list[GameObject]:
    return for_render