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

        self.state = random.randint(1, 3) #the value of the self.objects are just a subclass of the class object attribute that will be created soon
        self.type = random.randint(1, 2)
        self.hardness = random.randint(1, 10) * self.state

#rocks have 3 states: fresh, crackled, destroyed
#the player can get the rock position and type, the type deetermines the hardness of the rock
class Rock(Entity):
    def __init__(self, pos=(0, 0)):
        super().__init__("rock.jpg", pos)
        self.state = random.randint(1, 3)
        self.type = random.randint(1, 2)
        self.hardness = random.randint(1, 10)*self.state

    def pos(self):
        return self.pos
    def state(self):
        return self.state
    def type(self):
        return self.type

class Wall(Entity):
    def __init__(self, pos=(0, 0)):
        super().__init__("wall.png", pos)
        self.state = random.randint(1, 3)
        self.type = random.randint(1, 2)
        self.hardness = random.randint(1, 10) * self.state
    def pos(self):
        return self.pos
    def state(self):
        return self.state
    def type(self):
        return self.type

class Press(Entity):
    def __init__(self, pos=(0, 0)):
        super().__init__("press.png", pos)
        self.compacting_power = 1
    def compact(self, state):
        return state + self.compacting_power











SHIP = Ship()
ROCK = Rock()
WALL = Wall()


def get_for_render() -> list[GameObject]:
    return for_render