num=int(input("enter the number :"))
for i in range(1, 11):
    print(num,"*",i,"=",num * i)

n = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("The factorial of number is: " ,factorial)

n = int(input("Enter the number of terms: "))
a=0
b = 1
print("Fibonacci sequence up to", n, "terms:")
count = 0
while count < n:
    print(a, end=' ')

    c = a + b
    a = b
    b = c
    count += 1


str = input("Enter a string: ")
vowels = "aeiouAEIOU"
v = 0
for i in str:
    if i in vowels:
        v = v+1
print("the number of vowel is:", v)


numbers = [5, 2, 9, 1, 5, 6]
largest = numbers[0]
smallest = numbers[0]

i = 1
while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    elif numbers[i] < smallest:
        smallest = numbers[i]
    i += 1



num = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 8, 9, 7]

a = []

i = 0
while i < len(num):
    
    if num[i] not in a:
   
        a.append(num[i])
  
    i += 1
print("Original List:",num)
print("List with Duplicates Removed:",a)


print("Largest element in the list:",largest)
print("Smallest element in the list:",smallest)
import math

# Input number to find square root
number = float(input("Enter a number to find its square root: "))

# Check if the number is negative
if number < 0:
    print("Square root of negative numbers is not defined.")
else:
    # Calculate square root using math.sqrt
    square_root = math.sqrt(number)
    # Print the result
    print(f"The square root of {number} is approximately {square_root:.6f}")
