year=int(input("enter the year"))
if (year%400==0) or (year%40==0 and year%100!=0):
    print("it is leap year")
else:
    print("it is not a leap year")

 