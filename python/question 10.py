num1 = 10
num2 = 30
num3 = 20

if (num1 <= num2) and (num1 <= num3):
    minimum = num1
elif (num2 <= num1) and (num2 <= num3):
    minimum = num2
elif (num3 <= num1) and (num3 <= num2):
    minimum = num3
print("the minimum number is ", minimum)
