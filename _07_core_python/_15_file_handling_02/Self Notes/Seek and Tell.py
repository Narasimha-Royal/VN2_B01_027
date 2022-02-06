a = open("seek.txt", 'r')
a.seek(23, 0)
print(a.tell())
print(a.readline())
a.close()

print("---------Using Binary Format---------")

b = open("seek.txt", 'rb')
b.seek(-21, 2)
print(b.tell())
print(b.read())
b.close()
