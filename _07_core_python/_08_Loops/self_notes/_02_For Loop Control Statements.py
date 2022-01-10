print("-----------Control Statements----------")
print("-----1) Break Statement-----")
a = "Narasimha"
for i in a:
    print(i)
    if i == 's':
        break
print("-----2) Continue Statement-----")
b = 50
for i in range(1, b):
    if i % 5 == 0:
        continue
    print(i)
print("-----3) Pass Statement-----")
c = 40
if c > 20:
    pass
