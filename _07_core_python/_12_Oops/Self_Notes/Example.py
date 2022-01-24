class Dinner:

    def __init__(self):
        print("Enter Menu Numbers '1 or 2 or 3'")

    def price(self, menu):
        if menu == 1:
            print("Price for 'menu1' is 15.00 Rupees")
        elif menu == 2:
            print("Price for 'menu2' is 17.00 Rupees")
        elif menu == 3:
            print("Price for 'menu3' is 20.00 Rupees")
        else:
            print("Please Enter Valid menu number")


a = Dinner()
b = int(input("Enter Menu Number :"))
a.price(b)
