print("Assignment Operators")
a = 10
a += 5
print(a)
a -= 5
print(a)
a *= 5
print(a)
print("Logical Operators")
b = 4
print(b > 1 and b < 10)
print(b > 1 and b > 10)
print(b > 2 or b > 10)
print("Membership Operators")
c = ["Royal","Charan","Lokesh"]
print("Royal" in c)
print("Charan" not in c)
print("Identity Operators")
d = ["shiva","naveen"]
e = ["shiva","naveen"]
f = d
print(d is f)
print(d is e)
print(d == e)