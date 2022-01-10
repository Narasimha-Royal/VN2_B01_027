print("-----If Statements using Arithmetic Operators with Integers-----")
a = 10
b = 20
if a+b :
    print("Addition of two integers:",a + b)
if b-a :
    print("Substract a from b:",a - b)
if a * b :
    print("Multiplication of two integers:",a * b)
if b / a :
    print("Divides b by a:",b / a)
if b % a :
    print("Divides b by a and returns reminder:",b % a)
if a ** b :
    print("a power of b:",a ** b)
if a // b :
    print("Floor division of a//b :",a // b)

print("-----If Statements using Comparison Operators with Integers and Strings-----")
c = 50
d = 60
e = "narasimha"
if c == d :
    print("c and d are equal")
if c != d :
    print("c and d are not equal")
if c > d :
    print("c is greater than d")
if c < d :
    print("c is lesser than d")
if c >= d :
    print("c is greater than or equal to d")
if c <= d :
    print("c is lesser than or equal to d")
if e == 'narasimha' :
    print("Thank You")
if e == 'simha' :
    print("Check the string")


print("-----If Statements using Logical Operators with Integers-----")
m = 50
n = 70
if m > 40 and n > 60 :
    print("And ondition executed")
if m < 40 and n > 60 :
    print ("And condition not satisfied")
if m > 40 or n > 60 :
    print("Or condition executed")
if m < 40 or n > 60 :
    print ("Or condition executed")
if not(m > 40 and n > 60 ) :
    print("Not condition executed")

print("-----If Statements using Identity Operators with Strings")
p = "charan"
q = "lokesh"
r = "charan"
if p is q :
    print("Strings are same")
if p is not q :
    print("Strings are different")
if p is r :
    print("Strings are same")

print("-----If Statements using Membership Operators with Lists or Sets")
s = [5,2.4,'royal',"narasimha"]
t = {7,1.3,'charan',"lokesh"}
if 'royal' in s :
    print("royal is in the List")
if 5 not in s :
    print("5 is not in List")
if 7 in t :
    print("7 is in the Set")
if 8 in t :
    print("8 is not the Set")


print("-----If Statements with None-----")
if False :
    print ("Nothing")
if None :
    print ("None")
if 0 :
    print ("Zero")