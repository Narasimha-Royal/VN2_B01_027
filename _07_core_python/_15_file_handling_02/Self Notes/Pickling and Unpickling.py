import pickle


class Details:
    def __init__(self, name, age, loc):
        self.name = name
        self.age = age
        self.loc = loc

    def display(self):
        print("Name is :{} \nAge is :{} \nLocation :{}\n".format(self.name, self.age, self.loc))


print("-------------Pickling------------")

a = open("data.dat", 'wb')
b = int(input("Enter Number of students :"))
for i in range(b):
    name = input("Enter Name :")
    age = int(input("Enter Age :"))
    loc = input("Enter Location :")
    c = Details(name, age, loc)
    pickle.dump(c, a)
a.close()


print("----------------Unpickling------------------")


d = open("data.dat", 'rb')
while True:
    try:
        f = pickle.load(d)
        f.display()
    except EOFError:
        break
