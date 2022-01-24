class Area:
    def __init__(self, sides):
        self.sides = sides

    def formula(self):
        print(self.sides + self.sides)


class Circle(Area):
    def __init__(self):
        Area.__init__()


value = Area(5)
value.formula()

class Note:
    def __init__(self, noot):
        print("Hi")
        self.toon = noot


a = Note(5)
print(a.toon)


