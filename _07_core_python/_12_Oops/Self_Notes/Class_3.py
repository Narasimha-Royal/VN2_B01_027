print("--------------Types of Methods----------------")

print("----Using Instance Method And Class Method----")


class Bikes:
    company = "Royal Enfield"

    def __init__(self, name, model):
        self.name = name
        self.model = model

    # Using Instance Method (We can access both instance and Class Variables)

    def info(self):
        print("---Bike Details---")
        print("Bike Name is :", self.name, "\nBike Model is :", self.model, "\nBike Company is :", Bikes.company)

    # Using Class method (We can access only Class variables)
    @classmethod
    def details(cls):
        print("Your Bike Company is :", Bikes.company)


a = Bikes("Royal Enfield Bullet", "Bullet 350")
a.info()
Bikes.details()

b = Bikes("Royal Enfield Classic", "Classic 350")
b.info()
b.details()

c = Bikes("Royal Enfield Himalayan", "Himalayan 250")
c.info()
Bikes.details()
