print("Select Category \n 1.Commercial \n 2.Institutional \n 3.Domestic")
a = int(input("Enter the Category Number :"))
if a == 1:
    b = int(input("Enter the Number of Units required :"))
    if b > 0 and b <= 5000:
        print("Your bill for",b,"units in Rupees",1500)
    elif b > 5000 and b <= 10000:
        c = b - 5000
        print("Your bill for",b,"units in Rupees",(c*0.25)+1500)
    elif b > 10000 and b <= 20000:
        d = b - 5000
        print("Your bill for",b,"units in Rupees",(d*0.23)+1500)
    elif b > 20000:
        e = b - 5000
        print("Your bill for",b,"units in Rupees",(e*0.2)+1500)
    else:
        print("Enter Valid number of units")

elif a == 2:
    f = int(input("Enter the Number of Units required :"))
    if f > 0 and f <= 5000:
        print("Your bill for",f,"units in Rupees",1800)
    elif f > 5000 and f <= 10000 :
        g = f - 5000
        print("Your bill for",f,"units in Rupees",(g*0.3)+1800)
    elif f > 10000 and f <= 20000:
        h = f - 5000
        print("Your bill for",f,"units in Rupess",(h*0.28)+1800)
    elif f > 20000:
        j = f - 5000
        print("Your bill for",f,"units in Rupees",(j*0.25)+1800)
    else:
        print("Enter Valid number of units")


elif a == 3:
    l = int(input("Enter the Number of units Required :"))
    if l > 0 and l <= 100:
        print("Your bill for",l,"units in Rupees",75)
    elif l > 100 and l <= 200:
        m = l- 100
        print("Your bill for",l,"units in Rupees",(m*1.25)+75)
    elif l > 200 and l <= 400:
        n = l - 100
        print("Your bill for",l,"units in Rupess",(n*2)+75)
    elif l > 400:
        o = l - 100
        print("Your bill for",l,"units in Rupees",(o*2.5)+75)
    else:
        print("Enter Valid number of units")


else:
    print("Please Enter Valid Category Number")