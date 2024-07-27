x = int(input("What is your exam score?"))
if x >= 85:
    print('You got an A')
elif x >= 75:
    print('You got a B')
elif x > 50:
    print('You got a C. Not great')
elif x == 50:
    print('You got a D')
else:
    print("You did not pass the exam.")
