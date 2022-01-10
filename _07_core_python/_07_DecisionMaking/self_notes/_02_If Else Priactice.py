a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
if a > b:
    print(a,"is greater")
elif b > a:
    print(b,"is greater")
else:
    print("Enter non zero values")


print("Checking for Eligible or not for voting")
c = int(input("Enter age:"))
if c <= 0 :
    print("Enter valid age")
else :
    if c > 0 and c < 18 :
        print("Not eligible for voting")
    else :
        print("Eligible for voting")
