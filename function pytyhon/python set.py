# s1 = {1, 2, 5, 3, 2, "Ammar", "codianic", "hammad"}
# print(s1)

# s1.add("hawa")
# print(s1)

# s1.clear()
# print(s1)
# s1.remove("Ammar")
# print(s1)

# s1.pop()
# print(s1)
# s1 = {1, 2, 5, 3, 2, "Ammar", "codianic", "hammad"}
# s2={8,"ahmad","sana",9}
# s1.update(s2)
# print(s1)
# s1 = {1, 2, 5, 3, 2, "Ammar", "codianic", "hammad"}
# s2 = {8, "ahmad", "sana", 9}
# s3 = {"banana", "apple", "mango"}
# s3.discard("apple")
# print(s3)

# print(s1 | s2 | s3)

#join a set with tuple

# tuple1=(1,"python",True,2.5)
# s1 = {1, 2, 5, 3, 2, "Ammar", "codianic", "hammad"}
# x=s1.union(tuple1)
# print(x)
#intersection a set with tuple
# tuple1=(1,"python",True,2.5)
# s1 = {1, 2, 5, 3, 2, "Ammar", "codianic", "hammad"}
# x=s1.intersection(tuple1)
# print(x)

#use "&" to join two set
s1 = {1, 2, 5, 3, 2, "Ammar", "codianic", "hammad"}
s2 = {8, "ahmad", "sana", 9}
y=s1 & s2
print(y)