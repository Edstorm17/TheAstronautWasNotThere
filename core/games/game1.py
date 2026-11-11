from random import random
from core.entity.entities import Entity, Argon
import random
from core.math_utils import Vec2
from entity import entities
from item.items import items

seed = random.randint(32456234756427656,243764256782436724376)
e = {}
def new_level(world_size):
    world_size = [world_size, world_size]
    print("level 1 loaded")

    count = 0
    for i in range(world_size[0]):
        for j in range(world_size[1]):
            if random.randint(0, 1):
                curpos = Vec2(i, j)
                e[curpos] = Argon(pos = curpos)
                count +=1


def harvest(e):
    if entities.SHIP.get_pos() in e:
        e.pop(entities.SHIP.get_pos()).delete()
        items.gold.increment()
        return True
    else:
        print('nothin there')
