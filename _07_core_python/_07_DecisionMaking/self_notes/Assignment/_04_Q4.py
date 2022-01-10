a = int(input("Enter the Price :"))
if a > 10000 :
    b = a * 0.2
    print("Discount Price is",b)
    print("Price after Discount :",a - b)
elif a <= 10000 and a > 7000 :
    c = a * 0.15
    print("Discount Price is",c)
    print("Price after Discount :",a - c)
else :
    d = a * 0.1
    print("Discount Price is",d)
    print("Price after Discount :",a - d)