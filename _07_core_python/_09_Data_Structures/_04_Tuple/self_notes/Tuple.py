print("---------Tuple-------")

t = (23, 45, 89, 15, 56, 61,)
s = (11, 72, 99, 34, 77)
print("Tuple 1 :", t)
print("Tuple 2 :", s)
print("Adding Tuples :", t + s)
print("Multiplying Tuple :", s * 3)
print("Length of Tuple :--", len(t))
print("Maximum in Tuple :--", max(t))
print("Minimum in Tuple :--", min(t))

print("------------------------------------")
print("----------Tuple Functions-----------")

a = (23, 45, 65, 89, 15, 72, 99, 45, 34, 77, 345, 462, 45)

print("------1) Using Count Function-------")   #Returns the number of times a specified value occurs in a tuple
print("Number of Count '45' in given Tuple :--", a.count(45))

print("------2) Using Index Function-------")   #Searches the tuple for a specified value and returns the position of where it was found
print("Index Value of '77' in given Tuple :--", a.index(77))

print("----------------------------------")
print("----------Loops in Tuple----------")

b = (34, 6.5, 47, 988, 'Royal', True)
for i in b:
    print(i)

print("----------------------------------")
for i in range(len(b)):
    print(i, ":", b[i])
