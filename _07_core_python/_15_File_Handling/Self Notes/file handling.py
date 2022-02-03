for i in range(65, 91):
    a = str(chr(i)+".txt")
    b = open(a, 'w')
    b.write("this is file")
#    a = open(chr(i), 'w')
#    a.write("This is file")
