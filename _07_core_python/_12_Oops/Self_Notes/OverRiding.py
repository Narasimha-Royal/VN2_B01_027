class Vehicle:
    def __init__(self, name, model):
        self.vname = name
        self.vmodel = model

    def type(self):
        print(self.vname, self.vmodel)


class Bike(Vehicle):
    def __init__(self, name, model):
        Vehicle.__init__(self, name, model)
        self.wheels = "2 Wheels bike"

    def type(self):
        print(self.vname, self.vmodel)

    def new(self):
        print(self.vname, self.vmodel, self.wheels)


a = Vehicle("RE", "Bullet")
a.type()

b = Bike("Royal Enfield", "Classic")
b.type()
b.new()

