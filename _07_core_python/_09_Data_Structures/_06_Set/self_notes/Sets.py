a = {1, 9, 'Royal', 4.5, False, 452, 56}
print("Given Set is :--", a)
print("Type of 'a' is :", type(a))
print("Length of Set is :--", len(a))

print("----Using Membership Keyword----")
print("'Royal' is present in the set or not :--", "Royal" in a)

print("-----Accessing items in Set Using 'For' Loop-----")
for i in a:
    print(i)
