print("------Reversing Tuple------")
t = (23, 45, 5.4, True, 65, 'Royal', 89, 15, 72)


def rev(t):
    new_t = t[::-1]
    return new_t


print("Original Tuple :", t)
print("Reverse of given Tuple :", rev(t))

print("-------Size of Tuple--------")
print("Size of Tuple :--", t.__sizeof__(), "bytes")

print("-----Changing The Tuple Items-----")
'''To change tuple items convert the tuple into a list, change the list, and convert the list back into a tuple.'''
print("Original Tuple :", t)
a = list(t)
a.append(11111111)
a.insert(3, 'charan')
a.remove(65)
t = tuple(a)
print("After Updating Items in Tuple :", t)

print("-----1) Using All Function-----")
'''The all() function is an inbuilt function in Python which returns true if all the elements of a given 
iterable are True else it returns False.'''

c = (56, 3.6, 4, 'hello')
print(all(c))
d = (565, 342, 6.55, 0)
print(all(d))

print("-----2) Using Enumerate Function-----")
'''Enumerate method adds a counter to an iterable and returns it in a form of enumerating object'''
print(enumerate(c))
print(tuple(enumerate(c)))
