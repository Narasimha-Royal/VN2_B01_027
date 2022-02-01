import pdb


def create_adder(x):
    def adder(y):
        return x + y

    return adder


pdb.set_trace()
add_15 = create_adder(15)
print(add_15(10))
