from __future__ import annotations
class Vec2:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        if isinstance(x, tuple):
            self.x = x[0]
            self.y = x[1]
        self.x = x
        self.y = y
    def __add__(self, other: Vec2 | float) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Vec2(self.x + other[0], self.y + other[1])
        return Vec2(self.x + other, self.y + other)
    def __iadd__(self, other):
        return self + other
    def __radd__(self, other: Vec2 | float) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Vec2(self.x + other[0], self.y + other[1])
        return Vec2(self.x + other, self.y + other)
    def __sub__(self, other: Vec2 | float) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        elif isinstance(other, tuple):
            return Vec2(self.x - other[0], self.y - other[1])
        return Vec2(self.x - other, self.y - other)
    def __isub__(self, other):
        return self - other
    def __rsub__(self, other : tuple):
        if isinstance(other, tuple):
            return Vec2(other[0] - self.x, other[1] - self.y)
        return NotImplemented
    def __mul__(self, other: Vec2 | float) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        elif isinstance(other, tuple):
            return Vec2(self.x * other[0], self.y * other[1])
        return Vec2(self.x * other, self.y * other)
    def __imul__(self, other):
        return self * other
    def __truediv__(self, other: Vec2 | float) -> Vec2 :
        if isinstance(other, Vec2):
            return Vec2(self.x / other.x, self.y / other.y)
        elif isinstance(other, tuple):
            return Vec2(self.x / other[0], self.y / other[1])
        return Vec2(self.x / other, self.y / other)
    def __itruediv__(self, other):
        return self / other
    def __hash__(self):
        return hash((self.x, self.y))
    def __iter__(self):
        yield self.x
        yield self.y
    def __eq__(self, other : Vec2):
        return self.x == other.x and self.y == other.y
    def min(self, other : float) -> Vec2:
        return Vec2(min(self.x, other), min(self.y, other))
    def max(self, other : float) -> Vec2:
        return Vec2(max(self.x, other), max(self.y, other))
