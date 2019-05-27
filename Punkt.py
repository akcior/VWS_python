class Punkt:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def get_lokacja(self):
        return Punkt(self.x, self.y)

    def translacja(self, x, y):
        self.x += x
        self.y += y

    def __eq__(self, other):
        if isinstance(other, Punkt):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Punkt):
            return Punkt(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __truediv__(self, other):
        try:
            return Punkt(int(self.x / other.x), int(self.y / other.y))
        except ZeroDivisionError as zex:
            print(zex)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
