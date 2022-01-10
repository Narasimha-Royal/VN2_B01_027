a = {'id': 27,
     'Name': ['Narasimha', 'Royal'],
     'Age': 21,
     'Mobile': 12345678,
     'Address': {'H.No': 111, 'Town': 'Kurnool'}}

print("Dictionary is :--", a)
print(type(a))
print(a['Name'])
print(a['Address']['Town'])
print("The Value of 'Mobile' key in given Dictionary :--", a['Mobile'])
print("Length of Given Dictionary is :--", len(a))

print("--------If Statement in Dictionary--------")
if 'Age' in a:
    print("Yes, Age is in the given Dictionary")

print("-------Updating Dictionary without Functions------")
print("Dictionary Before Updating :--", a)
a['Age'] = 22
print("Dictionary After Updating  :--", a)

print("------Add Items to Dictionary------")
print("Dictionary Before Updating :--", a)
a['Role'] = 'Engineer'
print("Dictionary Before Updating :--", a)

print("-----Loops in Dictionary-----")
print("-----Loop for Keys-----")
for i in a:
    print(i)
print("-----Loop for Values-----")
for i in a:
    print(a[i])
