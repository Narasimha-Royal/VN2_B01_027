class Birds:
    def __init__(self, name, color):
        self.name = name
        self.color = color


p1 = Birds("Parrot", "Green")
p2 = Birds("Duck", "Yellow")
print(p1.name, "Color is", p1.color)
print(p2.name)

# -------------------------------------------------------------

print("---------------------------------------------------------")


class Shapes:
    c = "Circle"
    s = "Square"

    def shape(str):
        print("Shape of 'c' is", str.c, "and Shape of 's' is", str.s)


a = Shapes()
a.shape()

# --------------------------------------------------------------------------

print("-------------------------------------------------------------------")


class Animals:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def details(self):
        print(self.name, "color is", self.color)


p1 = Animals("Lion", "Yellow")
p2 = Animals("Elephant", "Grey")
p1.details()
print(p2.name)

# -------------------------------------------------------------------

print("-------------------------------------------------------------------")


class Mobiles:
    def __init__(design, name, model):
        design.name = name
        design.model = model

    def phone(brand):
        print(brand.name, brand.model)


b = Mobiles("Nokia", 2022)
c = Mobiles("Samsung", 2021)
b.phone()
print(c.name)

print("----------Perimeter of Triangle Using OOPs-----------")

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def prmt(val):
        d = val.a + val.b + val.c
        print("Perimeter of Triangle is :--", d)

c = Triangle(5, 6, 7)
c.prmt()