class Details:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Basic Details :", self.name, self.age)


class Information(Details):
    def __init__(self, name, age, loc, no):
        Details.__init__(self, name, age)
        self.loc = loc
        self.no = no

    def detail(self):
        print("Full Details are", self.name, self.age, self.loc, self.no)


a = Information("Charan", 22, "NEL", 11)
a.info()
