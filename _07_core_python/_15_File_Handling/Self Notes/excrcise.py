a = open("info.txt", 'r')
b = a.readlines()
c = int(input("Enter any Line Number :"))
if 0 < c <= len(b):
    print("Content in number", c, "line :--", b[c-1])
else:
    print("Invalid Line Number")
