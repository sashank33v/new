import json
from models.book import Book


class SimpleBook(Book):
    pass


class Library:

    def __init__(self):
        self.books = []

    # Composition
    def add_book(self, title, author):
        book = SimpleBook(title, author)
        self.books.append(book)
        self.save_books()

    def view_books(self):
        return self.books

    # Iterator
    def __iter__(self):
        return iter(self.books)

    # Generator
    def available_books(self):
        for book in self.books:
            if book.is_available():
                yield book

    # File Handling
    def save_books(self):

        data = []

        for book in self.books:
            data.append({
                "title": book.title,
                "author": book._author
            })

        with open("data.json", "w") as f:
            json.dump(data, f)

    def load_books(self):

        try:
            with open("data.json", "r") as f:
                data = json.load(f)

                for item in data:
                    book = SimpleBook(item["title"], item["author"])
                    self.books.append(book)

        except FileNotFoundError:
            print("No data file found")
