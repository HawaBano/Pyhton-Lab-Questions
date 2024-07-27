# Q2
# str = input("enter your name: ")
# try:
#     num = int(str)
#     print(num)
# except ValueError:
#     print('Please enter an integer')

# 6
# num=[3,6,1,9,8,4]
# try:
#     for x in num:
#         avg=sum(num)/len(num)
#         print(avg)
#         break
# except:
#     print("execption")

# dic={
#     "name":"hawa",
#     "f_name":"g_abbas",
#     "city":"rwp"
# }
# key=input("enter the key: ")
# try:
#     value=dic[key]
#     print("the value of key is : ",value)
# except:
#     print("the value is not found!")
# import math
# number = int(input("Enter a number: "))

# try:
#     if number >= 0:
#         sqrt = math.sqrt(number)
#         print(f"The square root of {number} is {sqrt:.2f}")
#     else:
#         print("Cannot calculate square root of a negative number.")

# except ValueError:
#     print("Invalid input. Please enter a valid number.")


filename = input("Enter the file name: ")
try:
    with open(filename ,'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        print("Number of lines in file: ",num_lines)
except FileNotFoundError:
    print("File' not found.")
