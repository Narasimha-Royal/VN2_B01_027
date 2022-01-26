class Operators:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return x+y


p1 = Operators(5, 6)
print(p1)


