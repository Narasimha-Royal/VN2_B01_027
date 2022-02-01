def total(a, b):
    c = a / b
    print(c)


try:
    total(6, 2)
    total(5, 0)
except ZeroDivisionError as j:
    print("Error in program :--", j)

print("--------Type Error---------")

try:
    total(4, 'a')
except TypeError as m:
    print(m)

print("---------Name Error-----------")

try:
    total(3, aa)
except NameError as k:
    print(k)
