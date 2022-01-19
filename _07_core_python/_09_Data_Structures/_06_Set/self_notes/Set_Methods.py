a = {5, "Royal", 56.1, False, 'Narasimha', 1999, "Nov"}
print("Given Set is :--", a)

print("-----1) Using Add Method-----")  # Adds an element to the set
print("Before adding element to set :--", a)
a.add(234213)
print("After  adding element to set :--", a)

print("-----2) Using Discard Method-----")
# Removes the specified element. If the item to remove does not exist, it will NOT raise an error.
print("Before Discarding element in set :--", a)
a.discard(56.1)
print("After Discarding  element in set :--", a)

print("-----3) Using Remove Method-----")
# Removes the specified element. If the item to remove does not exist, it will raise an error.
print("Before Removing element in set :--", a)
a.remove(False)
print("After  Removing element in set :--", a)

print("-----4) Using Pop Method-----")  # Removes an element from the set
print("Before using Pop the set is :--", a)
a.pop()
print("After using Pop the set is :--", a)

print("---------------Methods between two Sets---------------")
b = {'jan', 'feb', 'mar', 'apr', 'june'}
c = {'mar', 'june', 'aug', 'oct', 'nov'}
d = {'jan', 'feb', 'mar', 'apr', 'june'}
print("Set 1 is :--", b)
print("Set 2 is :--", c)
print("Set 3 is :--", d)

print("-----5) Using Difference Method-----")   # Returns a set containing the difference between two or more sets
print(b.difference(c))        # b - c
print(c.difference(b))        # c - b

print("-----6) Using Intersection Method-----")  # Returns a set, that is the intersection of two other sets
print(b.intersection(c))

print("-----7) Using Symmetric_Difference Method-----")  # Returns a set with the symmetric differences of two sets
print(b.symmetric_difference(c))

print("-----8) Using Union Method-----")  # Return a set containing the union of sets
print(b.union(c))

print("-----9) Using Difference_Update Method-----")
d = {'jan', 'feb', 'mar', 'apr', 'june'}
# Removes the items in this set that are also included in another, specified set
d.difference_update(c)     # b - c
print(d)

print("-----10) Using Intersection_Update Method-----")
# Removes the items in this set that are not present in other, specified set(s)
e = {'jan', 'feb', 'mar', 'apr', 'june'}
e.intersection_update(c)
print(e)

print("-----11) Using Symmetric_Difference_Update Method-----")
# inserts the symmetric differences from this set and another
f = {'jan', 'feb', 'mar', 'apr', 'june'}
f.symmetric_difference_update(c)
print(f)

print("-----12) Using Issubset Method-----")   # Returns whether another set contains this set or not
m = {100, 200, 300}
n = {400, 500, 600, 700, 100, 200, 300}
print(m.issubset(n))
print(n.issubset(m))

print("-----13) Using Issuperset Method-----")  # Returns whether this set contains another set or not
print(m.issuperset(n))
print(n.issuperset(m))

print("-----14) Using Isdisjoint Method-----")  # Returns whether two sets have a intersection or not
print(a.isdisjoint(m))
print(m.isdisjoint(n))
print(n.isdisjoint(m))

print("-----15) Using Update Method-----")  # Update the set with the union of this set and others
n.update(b)
print(n)

print("-----16) Using Copy Method-----")  # Returns a copy of the set
p = n.copy()
print(p)

print("-----17) Using Clear Method-----")  # Removes all the elements from the set
p.clear()
print(p)