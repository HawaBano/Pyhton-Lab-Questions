tuple1=(1,"python",True,2.5)
print(tuple1)
print(type(tuple1))
print(tuple1[1])

list1=["hawa",1,6534,False]
print(list1)



print(list1+list2)
print(list1*2+list2)

print(list1[2])

list1.reverse()
print(list1)

# #append the list

list1.append("codianic youtube channel")
print (list1)

list1.clear()
print(list1)

list2=["hammad","ali","sana"]
print(list2.copy())
print(list2.count("ali"))
list3=["sara","hina"]
list2.extend(list3)
print(list2)
print(list2.index("ali"))
list2.insert(1,"hawa")
print(list2)

print(list2.pop())
list2.remove("ali")
print(list2)

list2.sort