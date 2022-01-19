# sum of numbers
n1 = int(input("Enter Number n1 :--"))
n2 = int(input("Enter Number n2 :--"))


def sum(a, b):
    c = a + b
    return c


print("Sum of n1, n2 is :--", sum(n1, n2))

# --------------------------------------------------------------------------------------------------


# factorial of a given number


a = int(input("Enter Number :"))


def facto(x):
    b = 1
    for i in range(x, 0, -1):
        b = b * i
    print(b)


facto(a)
# ---------------------------------------------------------------------------


# sum of total elements in a list


a = [8, 2, 3, 0, 7]


def sum(x):
    b = 0
    for i in x:
        b = b + i
    print(b)


sum(a)

# -------------------------------------------------------------------------------

# Multiplication of total elements in a list


a = [8, 2, 3, -1, 7]

def multi(x):
    b = 1
    for i in x:
        b = b * i
    print(b)


multi(a)

# --------------------------------------------------------

# sum of total elements in a list given by user

a = []
for i in range(1, 6):
    b = int(input("Enter Numbers into list :"))
    a.append(b)


def sumof(x):
    c = 0
    for i in x:
        c = c + i
    print("Sum of total elements in given list is :--",c)

sumof(a)

# ----------------------------------------------------------------------------------------------------

# reverse of a string

a = input("Enter String :")


def rever(x):
    for i in range(len(x)-1, -1, -1):
        print(x[i], end="")


rever(a)

# ---------------------------------------------------------------------------------------------

# sum and sub of two numbers

a = int(input("Enter Number :"))
b = int(input("Enter Number :"))

def exe(x, y):
    c = a + b
    d = a - b
    return c, d

print((exe(a, b)))

# ---------------------------------------------------------------------------------

# using default argument

def defa(a, b = 9000):
    print("Name :", a, "Salary is", b)
defa('royal',5000)
defa('charan')

# -------------------------------------------------------------------------------

# printing even numbers into a list

def eve():
    a = []
    for i in range(4, 30):
        if i % 2 == 0:
            a.append(i)
    print(a)
eve()

# ----------------------------------------------------------------------------------

# sum, sub and multiplication of given numbers

def all(a, b):

    print("Sum is =", a+b)
    print("Sub is =", a-b)
    print("Multiplication is =", a*b)

a = int(input("Enter number :"))
b = int(input("Enter Number :"))
all(a, b)

# -------------------------------------------------------------


# present or absent in a list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def pre():
    if b in a:
        print("Present")
    else:
        print("Absent")


b = int(input("Enter Number :"))
pre()

# ----------------------------------------------------------------------------------

# maximum number 

def maximum():
    if a > b:
        if a > c:
            print(a, "Is maximum")
    elif b > c:
        print(b, "Is Maximum")
    else:
        print(c, "Is Maximum")
a = int(input("Enter Number a :"))
b = int(input("Enter Number b :"))
c = int(input("Enter Number c :"))
maximum()

# ------------------------------------------------------------------------

# even or odd numbers

def evod():
    if a % 2 == 0:
        print(a, "Is even")
    else:
        print(a, "Is odd")
a = int(input("Enter Number :"))
evod()

# -----------------------------------------------

# area of circle

def arec(a):
    print("Area of circle with radius", a, "is", 3.14 * (a ** 2))
a = int(input("Enter radius :"))
arec(a)

#-------------------------------------------------------------

# square of numbers in given range

def lis():
    a = []
    for i in range(1, 31):
        b = i * i
        a.append(b)
    print(a)
lis()

# ---------------------------------------------------------------------------------------


def arg(*a):
    print("my name is", a[1])


arg('royal', 'simha', 'charan')


def kargs(**a):
    print("My name is", a['fname'])


kargs(name='Royal', fname='Narasimha', lname='rrrrr')
