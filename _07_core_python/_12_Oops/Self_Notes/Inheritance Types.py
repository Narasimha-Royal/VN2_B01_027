print("-----Multiple Inheritance-----")


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(self.name, self.age)


class B:
    def info(self):
        print("Details from B Class")


class C(A, B):
    def information(self):
        print("Details from C class")


a = C("charan", 23)
a.information()
a.info()
a.details()


print("-----Multiline Inheritance-----")


class Fruits:
    def info(self):
        print("This is about fruits")


class Color(Fruits):
    def details(self):
        print("This is about fruit color")


class Name(Color):
    def information(self):
        print("This is about fruit name")


j = Name()
j.info()
j.details()
j.information()


print("-----Hierarchical Inheritance-----")


class Birds:
    def info(self):
        print("Birds have Wings")


class Parrot(Birds):
    def details(self):
        print("Parrot has RED Nose")


class Crow(Birds):
    def information(self):
        print("Crow has Black Feathers")


s = Parrot()
s.info()
s.details()

t = Crow()
t.info()
t.information()



