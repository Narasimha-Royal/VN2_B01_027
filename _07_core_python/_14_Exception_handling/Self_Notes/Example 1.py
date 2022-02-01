try:
    a = int(input("Enter Number :"))
    if a == 1:
        print("S")
    if a == 2:
        print("M")
    if a == 3:
        print("T")
    if a == 4:
        print("W")
    if a == 5:
        print("T")
    if a == 6:
        print("F")
    if a == 7:
        print("S")
    else:
        raise ArithmeticError
except:
    print("Enter Valid Number")
