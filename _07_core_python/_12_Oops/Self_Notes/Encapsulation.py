class Employee:
    def __init__(self, name, role, loc):
        self.name = name
        self.role = role
        self.loc = loc

    def info(self):
        print(self.name, self.role)

    def details(self):
        print(self.loc)


a = Employee("Charan", "Developer", "NEL")
a.info()
a.details()
