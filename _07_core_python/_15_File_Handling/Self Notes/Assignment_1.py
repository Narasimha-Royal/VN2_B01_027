a = open("Data.txt", 'a')
b = int(input("Enter No of Persons :"))
for i in range(b):
    c = input("Enter Name :")
    d = int(input("Enter age :"))
    e = input("Enter Location :")
    g = "Your Name is :{}\nYour Age is :{}\nYour Location is :{}\n".format(c, d, e)
    a.writelines(g)
    # a.write(c), a.write(d), a.write(e)

a.close()
