a = int(input("Enter Total Number of Working Days:"))
b = int(input("Enter Total Number of days for absent:"))
c = a - b
d = (c/a)*100
# e = "{:.2f}".format(d)
print("Your percentage is:",d,"%")
if d >= 75 :
    print("You are eligible for exam")
else:
    print("You are not eligible for exam")