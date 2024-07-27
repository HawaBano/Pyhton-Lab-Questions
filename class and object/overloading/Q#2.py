# Create a StringManipulator class with overloaded methods for concatenation. The methods should handle concatenation of strings and lists of strings.
from multipledispatch import dispatch


class StringManipulator:
    @dispatch(str, str)
    def concate(self, a, b):
        print(f"the concatination of two string is : {a + b}")

    @dispatch(list, str)
    def concate(self, a, b):
        print(f"the concatination of list and strinf is: {''.join(a) + b}")

    @dispatch(list)
    def concate(self, a):
        print(f"the concatination of the list is {''.join(a)}")


manupilat = StringManipulator()
manupilat.concate("hello!", "sara")
manupilat.concate(["hello", 'sara', "zara"], "ali")
manupilat.concate(["ali", "sara", "sana"])
