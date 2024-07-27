# Design a Library class with attributes for books (a list) and methods to add, remove, and search for books by title. Use another class Book with attributes for title, author, and ISBN.
class Book:
    title = ''
    author = ''
    ISBN = 0

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN


class Library:
    books = []

    def add(self, title, author, ISBN):
        book = Book(title, author, ISBN)
        self.books.append(book)

    def remove(self, ISBN):
        for index in range(0, len(self.books)):
            if (self.books[index].ISBN == ISBN):
                self.books.pop(index)
                print("Book has been removed")
                break

    def display_books(self):
        for book in self.books:
            print(f"""
**************** Book Info ****************
    Book Name: {book.title}
    Book Author: {book.author}
    Book ISBN: {book.ISBN}
""")

    def search(self, author):
        flag = False
        for book in self.books:
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
