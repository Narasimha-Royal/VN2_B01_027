a = {1: 45, 2: 56, 5: 98, 3: 34, 4: 34}
print("Given Dictionary is ", a)
print("After sorting the Keys in Dictionary")
for i in sorted(a.keys()):
    print(i, ":", a[i],)

#for i in sorted(a.values()):
    #print(i)

print("----------------------------------------")
print("After sorting the Values in Dictionary")
print(sorted(a.items(), key=lambda a: (a[1], a[0])))

print("-------------Reverse Dictionary------------------")

print("Original Dictionary :", a)
c = dict(reversed(a.items()))
print("Reverse Dictionary :", c)

#d = sorted({ele for val in a.values() for ele in val})
#print(d)

#e = (a.keys()) + (a.values())
#print(e)
print("---------Two Dictionaries---------")
b = {1: 32, 2: 33, 3: 78, 7: 345}
a.update(b)
print(a)
