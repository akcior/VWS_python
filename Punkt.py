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

    def __add__(self, other):
        if isinstance(other, Punkt):
            return Punkt(self.x + other.x, self.y + other.y)
        return NotImplemented
