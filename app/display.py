from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplay(Display):
    def __init__(self, book: Book):
        self.book = book

    def display(self):
        print(self.book.content)


class ReverseDisplay(Display):
    def __init__(self, book: Book):
        self.book = book

    def display(self):
        print(self.book.content[::-1])
