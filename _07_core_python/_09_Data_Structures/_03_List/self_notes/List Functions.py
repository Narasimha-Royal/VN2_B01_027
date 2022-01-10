print("-----------List--------------")

a = [1, 5.6, 'Royal', [2, 4.5], ('sai',True)]
print("Given List is :", a)

print("-------List Functions--------")

print("---1) Using Append Function---")  #Adds an element at the end of the list
print("Before append given list is :", a)
a.append('siva')
print("After append given list is  :", a)

b = [2, 1, 5, 456, 'charan', 6.7]
print("---2) Using Extend Function---") #Add the elements of a list (or any iterable), to the end of the current list4
print("Before Extend given list is :", b)
b.extend([67, 56, 'lokesh', 3.3])
print("After Extend given list is  :", b)

c = [4, 7.8, 'narasimha', True]
print("---3) Using Insert Function---")  #Adds an element at the specified position
print("Before Insert given list is  :", c)
c.insert(2, 345643)
print("After Insert given list is   :", c)

d = [34, 45, 'naveen', 7.8, (34, 78)]
print("---4) Using Pop Function---")   #Removes the element at the specified position
print("Before Pop given list is  :", d)
d.pop(3)
print("After Pop given list is   :", d)

e = [26, 9.7, 45, ('royal', 34)]
print("---5) Using Remove Function---")  #Removes the item with the specified value
print("Before Remove given list is   :", e)
e.remove(45)
print("After Remove given list is    :", e)

f = [54, 43, 7.9, (5.6, 67)]
print("---6) Using Index Function---")  #Returns the index of the first element with the specified value
print("Given List is :", f)
print("Index of '43' in given list is :",f.index(43))

g = [1, 2, 4, 6, 7, 2, 8, 2, 3, 2, 4, 5, 4]
print("---7) Using Count Function---")  #Returns the number of elements with the specified value
print("Given List is :", g)
print("Number of count of '2' in given list :", g.count(2))
print("Number of count of '4' in given list :", g.count(4))

j = [1, 'royal', 6.4, (7, 2, 8, 2), 5, 4]
print("---8) Using Reverse Function---")  #Reverses the order of the list
print("Given List is :", j)
j.reverse()
print("Reverse of given List :",j)

k = [1, 6.4, 7, 2, 8, 2, 5, 4]
print("---9) Using Sort Function---")   #Sorts the list
print("Given List is :", k)
k.sort()
print("Sort of given List :", k)
k.sort(reverse=True)
print(k)

l = [1, 'royal', 6.4, (7, 2, 8, 2), 5, 4]
print("---10) Using Copy Function---") #Returns a copy of the list
m = l.copy()
print("Copy of given List :", m)


n = [6.4, (7, 2, 8, 2), 5, 4]
print("---11) Using Clear Function---")
print("Given List :", n)
n.clear()
print("After Clear the Given list :", n)


