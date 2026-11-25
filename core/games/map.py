from core.math_utils import Vec2
class Map:
    def __init__(self, world_size : Vec2):
        self.grid = []
        self.world_size = world_size
        for y in range(self.world_size.y):
            self.grid.append([])
            for x in range(self.world_size.x):
                self.grid[y].append(None)

    def __contains__(self, item):
        if self.grid[item.pos.y][item.pos.x] is not None:
            return True
        return False
    def __iter__(self):
        for y in range(self.world_size.y):
            for x in range(self.world_size.x):
                yield self.grid[y][x]
    def __eq__(self, other):
        for y in range(self.world_size.y):
            for x in range(self.world_size.x):
                return not self.grid[y][x] != other.grid[y][x]
        return True

