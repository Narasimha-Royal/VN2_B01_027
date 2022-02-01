class Test:
    def __init__(self, name, age, loc):
        self.name = name
        self.age = age
        self.loc = loc

    def first(self):
        print(self.name, self.age, self.loc)


a = Test("charan", 22, "NEL")
a.first()

print("-------------------------------------------------------------------")


class Testing:
    def __init__(self, firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname

    def _second(self):
        print(self._firstname, self._lastname)


b = Testing("Sai", "Kumar")
b._second()

print(b._lastname)
print(a.age)


class Tester(Testing):
    def details(self):
        print("This Sub Class")


c = Tester("Naveen", "Kumar")
c._second()

print(c._firstname)


print("--------------------------------------------------------------------------")


class TestRole:
    def __init__(self, namee, agee):
        self.namee = namee
        self.agee = agee

    def new(self):
        print(self.namee, self.agee)


d = TestRole("Noor", 23)
d.new()

print(b._firstname)
