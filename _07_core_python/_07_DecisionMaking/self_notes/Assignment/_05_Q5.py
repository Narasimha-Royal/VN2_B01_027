a = int(input("Enter number of days visited for Library :"))
if a > 0 and a <= 5 :
    print("Total Charge for Library is",a * 2)
elif a >= 6 and a <= 10 :
    print("Total Charge for Libraby is",a * 3)
elif a >= 11 and a <= 15 :
    print("Total Charge for Libraty is",a * 4)
elif a > 15 :
    print("Total Charge for Library is",a * 5)
else :
    print("Enter Valid number of Days")