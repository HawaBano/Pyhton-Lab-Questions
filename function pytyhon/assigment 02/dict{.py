# dict = {
#     "hawa", "bano",
#     "id", 20,
#     "city", "rwp"
# }
# list = list(dict.items())
# print(list)

stringList = ["DBMS", "System Software", "Python", "Java Basics", "Visual Studio Basics"]
def findLongestStr(stringList):

    longestStr = ""
    for string in stringList:
        if len(string) > len(longestStr):
            longestStr = string
    return longestStr
print("The longest string in the given list is", findLongestStr(stringList))