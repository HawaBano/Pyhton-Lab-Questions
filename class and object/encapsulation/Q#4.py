# Implement a Library class with private attributes for books. Ensure encapsulation by providing public methods to add, remove, and search for books.

class Library:
    __book = []

    def __init__(self, __book):
        self.__book = []

    def add(self, author, title):
        i = {"title": title, "auther": author}
        self.__book.append({title, author})
        print("book is added")

    def remove(self, title):
        for i in self.__book:
            if i[title] == title:
                self.book.remove(i)
                print("book is removed")
                return
        print("title not found")

    def search(self, title):
        for i in self.__book:
            if i[title] == title:
                print("book is found", i)
                return
        print("book is not found")


library = Library()
library.add_book("halim", "nimra ahmad")
library.add_book("rooh_e_yaram", "areej shah")
library.search("halim")
print(library.search())
library.remove_book("halim")
