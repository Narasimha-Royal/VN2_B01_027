a = 0
b = 0
for i in range(12, 38):
    if i % 2 == 0:
        a = a+i
    else:
        b = b+i
print("Total Sum of Even Numbers :", a)
print("Total Sum of Odd Numbers :", b)