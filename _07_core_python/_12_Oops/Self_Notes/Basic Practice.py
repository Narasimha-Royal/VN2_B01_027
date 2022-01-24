class Bio:
    def __init__(some, name, age, loc):
        some.name = name
        some.age = age
        some.loc = loc


a = Bio("sai", 21, "Kad")
print("Name is :--", a.name)
print("Age is  :--", a.age)

# ----------------------------------------------------------------------------------


class Details:
    def __init__(any, name, age, sal):
        any.name = name
        any.age = age
        any.sal = sal

    def Some(abc):
        print("My name is :--", abc.name, "And My Age is: --", abc.age)


b = Details("Charan", 22, 20000)
b.Some()

# -----------------------------------------------------------------------------

class Some:
    a = 10
    b = 30
    def any(tin):
        print("a and b is:--", tin.a, tin.b)


c = Some()
c.any()

# -------------------------------------------------------------------'''

class Royal:
    a = 5
    b = 8
    def som(self):
        print("First value is", self.a, "Second value is", self.b)
c = Royal()
c.som()


class Simha:
    def __init__(self, name, age):
        self.name = name
        self.age = age
a = Simha("siva", 23)
print(a.name)
print(a.age)

class Royal:
    def __init__(any, name, age):
        any.name = name
        any.age = age
    def some(otr):
        print("Name is", otr.name, "and Age is", otr.age)

a = Royal("charan", 22)
a.some()

class Triangle:
    def __init__(self, a , b, c):
        self.a = a
        self.b = b
        self.c = c
    def prmt(self):
        d = self.a + self.b + self.c
        print("Perimeter of Triangle is :--", d)

c = Triangle(5, 6, 7)
c.prmt()




