def count():
    try:
        a = open("passage.txt", 'r')
        b = a.readlines()
        c = 0
        for i in b:
            if i[0] == 'A':
                c += 1
        print("Count of words starts with 'a' letter :", c)
    except Exception as j:
        print(j)
    finally:
        print("-----Program Completed-----")


count()
