def lettercount():
    try:
        a = open("Demo.txt", 'r')
        b = a.read()
        c = 0
        d = 0
        for i in b:
            if i == 'a':
                c += 1
            elif i == 'i':
                d += 1
        print("Count of 'a' letters in file :", c)
        print("Count of 'i' letters in file :", d)

    except Exception as e:
        print(e)
    finally:
        print("-----Program Completed-----")


lettercount()
