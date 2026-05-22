from abc import ABC

class Book(ABC):
    total_books = 0

    def __init__(self, title, author):
        self.title = title          # public
        self._author = author       # protected
        self.__available = True     # private

        Book.total_books += 1

    def borrow(self):
        self.__available = False

    def return_book(self):
        self.__available = True

    def is_available(self):
        return self.__available

    @classmethod
    def get_total_books(cls):
        return cls.total_books
