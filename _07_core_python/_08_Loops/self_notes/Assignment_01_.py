a = int(input("Enter Value for a :"))
r = int(input("Enter Value for r :"))
n = int(input("Enter Value for n :"))
s = 0
for i in range(1, n+1):
    s = s + (a * (r**i))
print(s + a)