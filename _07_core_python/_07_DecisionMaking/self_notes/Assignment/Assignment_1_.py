sh = int(input("Enter Amount for Shorts :"))
p = int(input("Enter Amount for Pants :"))
sht = int(input("Enter Amount for T-Shirts/Shirts :"))

if sh <= 0 :
    print("Enter Valid Amount for Shorts")
else :
    if sh > 0 and sh <= 100 :
        print("Your bill is",sh)
    elif sh >=101 and sh <= 200 :
        e = 0.05 * sh
        print("You got 5% discount on Shorts",e)
        print("Your bill for Shorts",sh - e)
    elif sh >= 201 and sh <= 300 :
        f = 0.1 * sh
        print("You got 10% discount on Shorts",f)
        print("Your bill for Shorts",sh - f)
    else :
        g = 0.18 * sh
        print("You got 18% discount on Shorts",g)
        print("Your bill for Shorts",sh - g)


if p <= 0 :
    print ("Enter Valid Amount for Pants")
else :
    if p > 0 and p <=100 :
        a = 0.03 * p
        print ("You got 3% discount on Pants", a )
        print ("Your bill for Pants", p - a)
    elif p >= 101 and p <= 200 :
        b= 0.08 * p
        print ("You got 8% discount on Pants",b)
        print ("Your bill for Pants",p - b)
    elif p >= 201 and p <= 300 :
        c= 0.12 * p
        print ("You got 12% discount on Pants",c)
        print ("Your bill for Pants",p - c)
    else :
        d = 0.2 * p
        print ("You got 20 % discount on Pants",d)
        print ("Your bill for Pants",p - d)


if sht <= 0 :
    print("Enter Valid Amount for Shirts")
else :
    if sht > 0 and sht <=100:
        s = 0.05 * sht
        print("You got 5% discount on Shirts",s)
        print("Your bill for Shirts",sht - s)
    elif sht > 100 and sht <=200 :
        t = 0.1 * sht
        print("You got 10% discount on Shirts",t)
        print("Your bill for Shirts",sht - t)
    elif sht > 200 and sht <= 300 :
        u = 0.15 * sht
        print("You got 15% discount on Shirts",u)
        print("Your bill for Shirts",sht - u)
    else :
        v = 0.22 * sht
        print("You got 22 % discount on Shirts",v)
        print("Your bill for Shirts",sht - v)