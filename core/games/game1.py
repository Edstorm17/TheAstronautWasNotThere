from random import random
from core.entity.entities import Entity, Rock
import random

seed = random.randint(32456234756427656,243764256782436724376)
e = {}
def new_level(world_size):
    world_size = [world_size, world_size]
    print("level 1 loaded")


    count = 0
    for i in range(world_size[0]):
        for j in range(world_size[1]):
            if random.randint(0, 1):
                curpos = (i, j)
                e[curpos] = Rock(pos = curpos)
                count +=1


