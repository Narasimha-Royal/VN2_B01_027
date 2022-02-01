from multipledispatch import dispatch


@dispatch(int, int)
def addition(a, b):
    c = a + b
    print(c)


addition(5, 6)


@dispatch(int, float, int)
def adding(a, b, c):
    d = a + b + c
    print(d)


adding(5, 6.1, 7)


@dispatch(str, str, str)
def concat(e, f, g):
    j = e + f + g
    print(j)


concat("Ro", "Y", "@L")


@dispatch(str, int)
def product(k, p):
    print(k*p)


product("Royal", 4)

