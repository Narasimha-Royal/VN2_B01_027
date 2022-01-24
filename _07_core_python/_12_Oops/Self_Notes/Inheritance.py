# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class

# ---------------------------------------------------------------------------------

# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:
class A:
    def first(self):
        print("My Name is Narasimha.")

    def second(self):
        print("My Name is Charan. This is from Parent Class")


# Create a Child Class

# To create a class that inherits the functionality from another class, send the parent class as a parameter when
# creating the child class:


class B(A):

    def third(self):
        print("My Name is Sai")


a = A()
a.first()

b = B()
b.third()
b.second()
