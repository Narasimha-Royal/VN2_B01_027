a = ['Royal', 'Charan', 'Sai', 'Shiva', 'Naveen']
b = (12, 23, 34, 45, 56)

for c, d in zip(a, b):
    print(d, "--", c)


print("--------------Zipping----------------")

e = (1, 3, 4, 5, 6)
f = ['Royal', 'Charan', 'Sai', 'Shiva', 'Naveen']
g = "NOTES"
h = zip(e, f, g)
i = list(h)
print(i)

print("------------------Unzipping---------------------")
e, f, g = zip(*i)
print(e)
print(f)
print(g)
