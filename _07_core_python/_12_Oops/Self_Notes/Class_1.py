class Student:
    def __init__(self, name, no, marks):
        self.name = name
        self.no = no
        self.marks = marks

    def details(self):
        print("Student Name is :", self.name, "\nRoll Number is :", self.no, "\nTotal Marks :", self.marks)

    def grade(self, x):
        if m >= 90 and m <= 100:
            print("Grade for Given Subject is A")
        elif m < 90 and m >= 80:
            print("Grade for Given Subject is B")
        elif m < 80 and m >= 70:
            print("Grade for Given Subject is C")
        elif m < 70 and m >= 60:
            print("Grade for Given Subject is D")
        else:
            print("Grade for Given Subject is Fail")


m = int(input("Enter Marks of any subject :"))
a = Student("Charan", 11, 590)
a.details()
a.grade(m)

print("--------------------------------------")

b = Student("Sai", 12, 585)
m = int(input("Enter Marks of any subject :"))
b.details()
b.grade(m)
