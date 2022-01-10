a = {'Name': 'Narasimha',
     'Emp_Id': 27,
     'Location': 'Bangalore',
     'Mobile': 123456789}
print("The Dictionary is :--", a)

print("------1) Using Get Function------")   #Returns the value of the item with the specified keys and values.
print("The Value of Given Key in Dictionary is :--", a.get('Name'))
print("The Value of Given Key in Dictionary is :--", a.get('Location'))

print("-----2) Using Keys Function------")  #Returns a list containing the dictionary's keys
print("Total keys in given Dictionary :--", a.keys())

print("-----3) Using Values Function-----")  #Returns a list of all the values in the dictionary
print("Total values in given Dictionary :--", a.values())

print("-----4) Using Items Function-----")  #Returns a list containing a tuple for each key value pair
print("Total keys and values in Dictionary :--", a.items())

print("-----5) Using Update Function-----")  #Updates the dictionary with the specified key-value pairs
print("Before Updating Dictionary is :--", a)

print("After Updating a Value in Dictionary")
a.update({'Mobile': 987654321})
print("After  Updating Dictionary is :--", a)

print("After Updating with New Key, Value pair")
a.update({'Age': 22})
print("After  Updating Dictionary is :--", a)

print("-----6) Using Fromkeys Function-----")   #Returns a dictionary with the specified keys and value
b = a.fromkeys([1, 2, 3, 4], "Hello")
print(b)

print("-----7) Using Pop Function----- ")   #Removes the element with the specified key
print("Before deleting Key Dictionary is ", a)
a.pop('Emp_Id')
print("After deleting Key Dictionary is ", a)

print("-----8) Using Popitem Function-----")   #Removes the last inserted key-value pair
print("Before Using Popitem Function ", a)
a.popitem()
print("After Using Popitem Function ", a)

print("-----9) Using Copy Function-----")  #Returns a copy of the dictionary
b = a.copy()
print("Copy of Dictionary is :--", b)

print("-----10) Using Clear Function-----") #Removes all the elements from the dictionary
print("Before Clear Function :", b)
b.clear()
print("After Clear Function :", b)

print("-----11) Using Has_Key Function-----")  #This method return true if a given key is available in the dictionary, otherwise it returns a false.
print("Value", a.has_key('Name'))