i = 1
c = 0
while i < 50:
    if i % 5 == 0:
        c = c + 1
        print(i)
        if c == 7:
            break
    i = i + 1
