class Addition:
    def __init__(self, a):
        self.a = a

    def __add__(self, o):
        return self.a + o.a


a = Addition(10)
b = Addition(20)
c = Addition(50)
d = Addition(40)

print("Addition of a and b :--", a+b)
print("Addition of c and d :--", c+d)
