# l1 = [13,2,43,4,36,78,54,3,2,40]
# print(l1)

# l2=["graps","apple", "mango","banana","papaya" "cherry"]
# l2.sort()
# print(l2)
# print(l1+l2)

# Q29
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {}
# for key, value in d1.items():
#     d2[value] = key
# print("value after swap:", d2)
# l2=["graps","apple", "mango","banana","papaya" ,"cherry"]
# l2.reverse()
# print(l2)

##-------------------------------------------
##-------------------------------------------
# function proggram start here
# Q1
# num = [1, 2, 3, 4, 5]
# def average(num):
#     for i in num:

#         total = sum(num)/len(num)
#     print(total)
# average(num)

# name = input("enter the string :")

# Q2
# name = input("enter the string :")
# def reverse(name):
#     str = ''
#     for ch in name:
#         str = ch+str
#     print(str)
    


# reverse(name)



# Q6

# numbers=[3,4,9,8,6,7]
# def even_numbers(numbers):
#     even_list = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_list.append(num)

#     print("the even number in list is :",even_list)
# even_numbers(numbers)

# Q7
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def secLastNum(list1):

#      num = list1[-2]
#      print("The second-largest number of the list:",num)
# secLastNum(list1)

# Q8
# str = "hello"

# def count_characters(str):
#     count = {}
#     for i in str:

#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1

#     print ("the number of character is " ,count)
# count_characters(str)

# Q9
# num = [4, 7, 23, 8, 7, 2]


# def is_sorted_ascending(nums):

#     for i in range(len(nums) - 1):
#         if num[i] >= num[i+1]:
#             flag = 1
#             break
#     if flag == 0:
#         print(True)
#     else:
#         print(False)


# is_sorted_ascending(num)
# Q10
# num=[3,5,78,65,4]
# def square(num):
#     new_list = []
#     for i in num:
#         new_list.append(i ** 2)
#     print("the square of the new list is ",new_list)
# square(num)


##mixed topic start
##---------------------------------------------------
##---------------------------------------------------
# Q3
# tups = [("apple", 10), ("banana", 12), ("graps", 14),
#         ("watermelon", 20), ("ornage", 25), ("mango", 30)]


# def Convert(tups):
#     dictionary = {}
#     dir = dict(tups)
#     print(dir)


# Convert(tups)

# # Q4
# List = [2, 1, 2, 2, 1, 3]


# def common(List):
#     dict = {}
#     count, itm = 0, ''
#     for item in reversed(List):
#         dict[item] = dict.get(item, 0) + 1
#         if dict[item] >= count:
#             count, itm = dict[item], item
#     print(itm)


# List1 = [2, 1, 9, 7, 4, 3]
# List2 = [12, 1, 5, 6, 9, 8]
# l3 = set(List1).intersection(set(List2))
# print(l3)

# # Q46
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1.intersection(set2, set3, set4)
# print(myset)

# # Q48

# key = ["apple", "bananas", "cherry"]
# value = [40, 38, 94]
# l1 = dict(zip(key, value))
# print(l1)

# # Q45
# num = [2, 3, 7, 6, 92, 3, 2, 3]
# dup = set()
# r_item = []
# for x in num:
#     if x not in dup:
#         r_item.append(x)
#         dup.add(x)
# print(dup)

# # Q49
# s1 = {"a", "banana", "hawa", 50}
# s2 = {30, "banana", "a", 50}
# s3 = {"a", "apple", "banana", "mango", "charrey"}
# s4 = s1.intersection(s2, s3)
# print(s4)
