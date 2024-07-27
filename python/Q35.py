num = int(input("enter the number"))
if num % 3 == 0 and num % 5 == 0:
    print("the number is divisible by both 3 and 5 ")
elif num % 3 == 0 and num % 5 != 0:
    print("the number is divisible by 3 and not divisiblr by 5")
elif num % 3 != 0 and num % 5 == 0:
    print("the number is not divisible by 3 and divisible by 5")
else:
    print("the number is not divisible by both 3 and 5 ")
