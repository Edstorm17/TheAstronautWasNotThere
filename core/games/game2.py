from random import random
from core.entity.entities import Entity, Drill, Gold, Argon
import random
from core.math_utils import Vec2


map = []
def new_level2(world_size):
    world_size = [world_size, world_size]
    print("level 2 loaded")
    for i in range(world_size[0]):
        for j in range(world_size[1]):
            if random.randint(0,1) == 0:
                pos = Vec2(i, j)
                chosen_class = random.choice([Gold, Argon])
                item = chosen_class(pos)
                map.append(item)
    count = len(map)
