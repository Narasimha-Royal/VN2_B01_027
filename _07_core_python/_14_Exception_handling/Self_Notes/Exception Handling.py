print("------Exception Handling--------")
try:
    a = 10
    b = 0
    c = a/b
    print("C value is", c)

except:
    print("Error in program")


print("-----------------------------------------")

try:
    a = 10
    b = 0
    c = a/b
    print("C value is", c)
except Exception as d:
    print("Error in program is :--", d)


print("------Multiple Exceptions------")

try:
    x = int(input("Enter First  Number :"))
    y = int(input("Enter Second number :"))
    z = x/y
    f = [1, 2, 3, 4]
    print(f[4])
    print("Z value is :", z)


except ZeroDivisionError as j:
    print("Error is :--", j)

except ValueError as k:
    print("Error is :--", k)

except IndexError as m:
    print("Error is :---", m)


print("-------------------------------------------------")

try:
    a = 5
    b = 2
    c = a/b
    print("C value is :--", c)

except:
    print("Error in program")

else:
    print("No errors in program")

finally:
    print("End of Program")


print("------------------------------------")
