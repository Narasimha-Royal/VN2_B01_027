class Example:
    def __init__(self, roll, name="Charan", sal="30000"):
        self.roll = roll
        self.name = name
        self.sal = sal
        print(self.roll, self.name, self.sal)


a = Example(21)
b = Example(22, "Sai")
c = Example(23, "Siva", 35000)
b = Example(24)
