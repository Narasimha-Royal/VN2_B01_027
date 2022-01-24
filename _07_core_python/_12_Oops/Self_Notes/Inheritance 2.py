class Vehicle:
    def __init__(self, name, model):
        self.vname = name
        self.vmodel = model

    def type(self):
        print("Vehicles are Used for Transportation")


class Bike(Vehicle):
    def info(self):
        print(self.vname, self.vmodel)

    def bikes(self):
        print("BIke is 2 wheeler")



b = Bike("Royal Enfield", "2 Wheeler")
b.type()
b.info()

print(isinstance(b, Bike))
# print(isinstance(c, Bike))

print(issubclass(Bike, Vehicle))

print(issubclass(Vehicle, Bike))

