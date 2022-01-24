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
        self.__firstname = firstname
        self.__lastname = lastname

    def second(self):
        print(self.__firstname, self.__lastname)


b = Testing("Sai", "Kumar")
b.second()
print(b.__firstname)


class Tester(Testing):
    def details(self):
        print("This Sub Class")


c = Tester("Naveen", "Kumar")
c.second()

# print(c.__firstname)

print(a.age)
a.age = 5
print(a.age)


print("--------------------------------------------------------------------------")


class TestRole:
    def __init__(self, namee, agee):
        self.namee = namee
        self.agee = agee

    def new(self):
        print(self.namee, self.agee)


d = TestRole("Noor", 23)
d.new()

c.second()

