a = 2
b = 4
c = 7

if (a > b & a > c):
    print("the largest value is ",a)
elif (b > a & b > c):
    print("the largest value is ",b)
elif (c > a & c > b):
     print("the largest value is ", c)
else:
    print("your value is invalid")

    while True:
    user_input = input("Please enter something (enter 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    # You can add more processing or actions based on user_input here if needed
    print(f"You entered: {user_input}")

print("Exiting the program.")
