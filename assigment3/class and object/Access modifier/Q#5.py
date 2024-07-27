# Create a Library class with private attributes for books (a list of Book objects). Implement public methods to add, remove, and search for books.
class Book:
    title = ''
    author = ''
    ISBN = 0

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN


class Library:
    __books = []

    def add(self, title, author, ISBN):
        book = Book(title, author, ISBN)
        self.__books.append(book)

    def remove(self, ISBN):
        for index in range(0, len(self.__books)):
            if (self.__books[index].ISBN == ISBN):
                self.__books.pop(index)
                print("Book has been removed")
                break

    def display_books(self):
        for book in self.__books:
            print(f"""
**************** Book Info ****************
    Book Name: {book.title}
    Book Author: {book.author}
    Book ISBN: {book.ISBN}
""")

    def search(self, author):
        flag = False
        for book in self.__books:
            if (book.author == author):
                flag = True
                break
            else:
                flag = False

        if (flag):
            print("Book Found")
        else:
            print("Book not found")


library = Library()
library.add("book1", "author1", 9854)
library.add("book2", "author2", 7855)
library.add("book3", "author3", 9765)
library.display_books()
library.remove(7855)
library.display_books()
library.search("author3")
