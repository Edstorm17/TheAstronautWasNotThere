from random import random
import random
from core.gamelayer import GameObject

for_render = []

class Entity(GameObject):
    def __init__(self, image, pos, dimensions=(1, 1)):
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



class Rock(Entity):
    def __init__(self, pos=(0, 0)):
        super().__init__("rock.jpg", pos)
        self.hardness = random.randint(1, 10)
        self.type =  random.randint(1, 2)
        self.state = [0,1,2]





class Wall(Entity):
    def __init__(self, pos=(0, 0)):
        super().__init__("wall.png", pos)
        self.hardness = random.randint(1, 10)
        self.type = random.randint(1, 2)








SHIP = Ship()
ROCK = Rock()
WALL = Wall()


def get_for_render() -> list[GameObject]:
    return for_render