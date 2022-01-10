a = int(input("Enter the percentage :"))
if  a <= 100 and a > 80 :
    print("A+ Grade")
elif a <= 80 and a > 60 :
    print("A Grade")
elif a <= 60 and a >50 :
    print("B+ Grade")
elif a <= 50 and a > 45:
    print("B Grade")
elif a <= 45 and a >= 25 :
    print("C Grade")
elif a < 25 and a >= 0 :
    print("D Grade")
else :
    print("Please Enter valid marks percentage")
