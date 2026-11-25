import random

from core.games.map import Map

from core.entity.entities import Argon, SHIP
from core.math_utils import Vec2
from item.items import items

seed = random.randint(32456234756427656,243764256782436724376)
map = Map(Vec2())

def new_level(world_size):
    global map
    world_size = Vec2(world_size, world_size)
    map = Map(world_size)
    print("level 1 loaded")

    for i in range(world_size.y):
        for j in range(world_size.x):
            if random.randint(0, 1):
                map.grid[i][j] = Argon(Vec2(j, i))

def harvest(items):
    player_pos = SHIP.get_pos().to_int()
    if map.grid[player_pos.y][player_pos.x]:
        item = map.grid[player_pos.y][player_pos.x]
        map.grid[player_pos.y][player_pos.x] = None
        item.delete()
        items['argon'].increment()
        for entity in map:
            if isinstance(entity, Entity):
                return True
        print("you win")
        g = image.load('assets/world_assets/press.png')
        #win(g)
        return True
    else:
        print('nothin there')
