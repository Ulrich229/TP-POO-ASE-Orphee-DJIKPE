class Person:
    """Class defining a person"""
    def __init__(self, first_name: str, last_name: str,) -> None:
        self.first_name = first_name.capitalize()
        self.last_name = last_name.upper()

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}"

class Book:
    """To implement"""
    def __init__(self, author: Person, title: str,) -> None:
        self.author = author
        self.title = title


class LibraryError(Exception):
    """Base class for Library errors"""


class Library:
    """To implement."""


def main():
    """Test your code here"""


if __name__ == "__main__":
    main()
