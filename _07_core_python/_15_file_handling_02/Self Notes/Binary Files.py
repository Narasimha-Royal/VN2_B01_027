a = open("python.jpg", 'rb')
b = open("binary.jpg", 'wb')
c = a.read()
# for i in c:
#    b.write(c)
b.write(c)
a.close()
b.close()
