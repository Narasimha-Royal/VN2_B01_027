print("--------For Loop in Integers with Break Statement--------")
a = 10
for i in range(1, a):
    print(i+i)
print("--------For Loop with Strings--------")
b = 'Narasimha'
for i in b:
    print(i*5)
print("------For Loop with List-------")
c = [2, 4.5, 'hello', [3, 'python'], (1, 9.8)]
for i in c:
    print(i*3)
print("-------For Loop with Dictionary-------")
d = {'E_id': 27, 'Name': 'Royal', 'Location': 'Bangalore'}
for i in d:
    print(i)
for i in d.values():
    print(i)
for i in d.keys():
    print(i)
for i in d.items():
    print(i)
