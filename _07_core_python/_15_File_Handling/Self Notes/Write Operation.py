a = open("Demo.txt", 'w')
a.write("This is Write operation")
a.close()

b = open("Demo.txt", 'a')
b.write("\nThis is new line")
b.close()

c = open("Demo.txt", 'r')
print(c.read())
c.close()


print("----------------------------------")

d = open("Demo.txt", 'r')
for i in d:
    print(i)
d.close()

print("----------------------------------")

with open("Demo.txt", 'r') as k:
    j = k.read()
    print(j)
k.close()


print("--------File Handling and Exception Handling--------")

try:
    with open("Demo1.txt", 'r') as a:
        print(a.read())
except Exception as a:
    print(a)
finally:
    print("---END---")
