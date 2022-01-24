print("---------Class Variables---------")

print("-----Without Class Variables-----")


class Details:
    def __init__(self, name, age, loc, country):
        self.name = name
        self.age = age
        self.loc = loc
        self.country = country

    def info(self):
        print("---Person Details---")
        print("Your name is :", self.name, "\nYour Age is :", self.age, "\nYour Location is :", self.loc,
              "\nYour County is :", self.country)


a = Details("Siva", 22, "KDP", "India")
a.info()
b = Details("Navin", 23, "DRM", "India")
b.info()


print("-----With Class Variables-----")


class About:
    country = "India"

    def __init__(self, name, loc, age):
        self.name = name
        self.loc = loc
        self.age = age

    def inform(self):
        print("---Person Details---")
        print("Your name is :", self.name, "\nYour Location is :", self.loc, "\nYour Age is :", self.age,
              "\nYour Country is :", About.country)


c = About("Sai", "KDP", 21)
c.inform()
d = About("Noor", "ATP", 22)
d.inform()
