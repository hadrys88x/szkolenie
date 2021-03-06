class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

vector1 = Vector(x=2,y=2)
vector2 = Vector(x=1,y=1)
vector3 = vector1 + vector2