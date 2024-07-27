x = int(input("Please enter a number"))
if ((x % 3 == 0) & (x % 5 == 0)):
  print("Your number is divisible by 3 and 5.")
  if ((x % 3 == 0) & (x % 5 == 1)):
    print("Your number is divisible by 3 and NOT 5.")
  elif ((x % 3 == 1) & (x % 5 == 0)):
    print("Your number is NOT divisible by 3 and is divisible by 5.")
else:
  print("Your number is NOT divisible by 3 and 5.")