print("Checking Online Products Based on Rating")
a = int(input("Enter Amount of Rating :"))
if a > 5 or a <= 0 :
    print("Enter a valid rating between 1 to 5")
elif a == 5 :
    print("Very Good products. Without thinking we can buy them.")
elif a == 4 :
    print("Good Products. We can buy them.")
elif a == 3 :
    print("Normal Products. We have to think to buy them")
elif a == 2 :
    print("Bad Products. No need to buy them.")
else :
    print("Very Bad Products. Don't buy them")