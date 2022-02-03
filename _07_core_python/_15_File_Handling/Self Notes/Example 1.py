a = open("Demo.txt", 'r')
b = open("New.txt", 'w')
c = open("append.txt", 'a')

# copy the data from one file to another file

for i in a:
    b.write(i)

b.close()

for i in a:
    c.write(i)
