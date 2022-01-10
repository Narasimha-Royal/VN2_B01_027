a = int(input("Enter the Employ Service in Years :"))
b = int(input("Enter the Employ Salary :"))
if a > 10 :
    c = b * 0.1
    print("Bonus Amount for salary",c)
    print("Total Salary with Bonus",c + b)
elif a <= 10 and a >= 6 :
    d = b * 0.08
    print("Bonus Amount for Salary",d)
    print("Total Salary with Bonus",d + b)
else :
    e = b * 0.05
    print("Bonus Amount for Salary",e)
    print("Total Salary with Bonus",e + b)