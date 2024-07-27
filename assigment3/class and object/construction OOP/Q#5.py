# Create a Bookstore class with a constructor to initialize a list of books and implement methods to add new books and find books by author.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)

    def find_books_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author == author:
                found_books.append(book)
        return found_books


b = Bookstore()
b.add_book("Book1", "Author1")
b.add_book("Book2", "Author2")
b.add_book("Book3", "Author1")
b.add_book("Book4", "Author3")
author = "Author1"
books_by_author = b.find_books_by_author(author)
print(f"Books by {author}:")
for book in books_by_author:
    print(f"{book.title} by {book.author}")
