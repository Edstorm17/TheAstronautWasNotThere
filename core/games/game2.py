from random import random
from core.entity.entities import Entity, Drill, Gold, Argon
import random



g = {}
def new_level2(world_size):
    world_size = [world_size, world_size]
    print("level 2 loaded")
    count = 0
    for i in range(world_size[0]):
        for j in range(world_size[1]):
            if random.randint(0,1) == 0:
                curpos = (i, j)
                chosen_class = random.choice([Gold, Argon])


                k = chosen_class(pos=curpos)
                g[curpos] = k
                count += 1
