from random import random
from core.entity.entities import Entity, Argon, SHIP
import random
from core.math_utils import Vec2
from entity import entities
from item.items import items

seed = random.randint(32456234756427656,243764256782436724376)
map = []
def new_level(world_size):
    world_size = [world_size, world_size]
    print("level 1 loaded")

    for i in range(world_size[0]):
        for j in range(world_size[1]):
            if random.randint(0, 1):
                map.append(Argon(Vec2(i, j)))
    count = len(map)


def harvest(e):
    player_pos = SHIP.get_pos()
    for item in map:
        if SHIP.get_pos() == item.pos:
            map.remove(item)
            item.delete()
            items.gold.increment()
        return True
    else:
        print('nothin there')
