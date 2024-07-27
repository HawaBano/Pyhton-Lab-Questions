#  Library Management System
# Question: Design and implement a Library management system. The system should have the following features:
# A Book class with attributes for title, author, ISBN, and availability status.
# A Member class with attributes for name, member ID, and a list of borrowed books.
# A Library class to manage books and members. Implement methods to add books, remove books, register members, and borrow/return books. Ensure that members cannot borrow more than a certain number of books and handle cases where books are not available.


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True



class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 5:
            print("Cannot borrow more than 5 books")
        else:
           book.available = False
           self.borrowed_books.append(book)
           print("Successfully borrowed")

    def return_book(self, book):
        if book not in self.borrowed_books:
            print("This book was not borrowed by you")
            book.available = True
        self.borrowed_books.remove(book)
        print("Successfully returned")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book
        return "Added book to the library"

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print("Removed book with ISBN")
        return "Book not found"

    def register_member(self, member):
        if member.member_id in self.members:
            print("Member already registered")
        self.members[member.member_id] = member
        return "Registered member"

    def borrow_book(self, member_id, isbn):
        if isbn not in self.books:
            return "Book not found"
        member = self.members[member_id]
        book = self.books[isbn]
        return member.borrow_book(book)

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            return "Member not registered"
        if isbn not in self.books:
            return "Book not found"
        member = self.members[member_id]
        book = self.books[isbn]
        member.return_book(book)
library = Library()

book1 = Book("Title1", "author1", "12345")
book2 = Book("title2", "author2", "67890")
print(library.add_book(book1))
print(library.add_book(book2))

member1 = Member("sara", "M001")
member2 = Member("sana", "M002")
print(library.register_member(member1))
print(library.register_member(member2))
library.borrow_book("M001", "12345")
library.return_book("M001", "12345")
library.remove_book("67890")
