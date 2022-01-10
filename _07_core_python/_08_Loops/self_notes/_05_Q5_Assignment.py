a = []
c = 0
for i in range(1, 100):
    if i % 2 == 0:
        a.append(i)
        c = c+1
        if c == 10:
            break
for i in a[::-1]:
    print(i)
