class Person:
    """Class defining a person"""
    def __init__(self, last_name: str, first_name: str,) -> None:
        self.first_name = first_name.upper()
        self.last_name = last_name.capitalize()

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}"

class Book:
    """Books definition"""
    def __init__(self, title: str,author: Person) -> None:
        self.title = title
        self.author = author
    
    def __str__(self) -> str:
        return f"{self.title} ({self.author})"


class LibraryError(Exception):
    """Base class for Library errors"""


class Library:
    """To implement."""
    def __init__(self, name: str) -> None:
        self.name = name
        self._books = []
        self._members = set()
        self._borrowed_books = {}

    def is_book_available (self,book: Book)-> bool:
        if(book in self._books):
            return True
        else:
            raise LibraryError("The book is not available")
    
    def borrow_book(self,book: Book, person: Person) -> None:
        if(person not in self._members):
            raise LibraryError("La personne qui essaye de prêter le livre n'est pas membre de la bibliothèque")
        elif (not self.is_book_available(book)):
            raise LibraryError("Le livre que vous essayez de prêter n'est pas dans notre catalogue")
        else:
            self._borrowed_books[book] = person

    def return_book(self,book: Book) -> None:
        if (book not in self._borrowed_books.keys):
            raise LibraryError("Le livre que vous essayez de rendre n'a pas été enrégistré comme prêté")
        else:
            self._borrowed_books.pop(book)


    def add_new_member(self, person:Person)-> None:
        self._members.add(person)
    
    def add_new_book(self, book:Book)->None:
        self._books.append(book)
    
    def print_status(self):
        available_books = []
        for book in self._books:
            if self.is_book_available(book):
                available_books.append(book)

        print(f"{self.name} status:")
        print(f"Books catalogue: {self._books}")
        print(f"Members: {self._members}")
        print(f"Available books: {available_books}")
        print(f"Borrowed books: {self._borrowed_books}")


def main():
    """Test your code here"""
    antoine = Person("Antoine", "Dupont")
    print(antoine)

    julia = Person("Julia", "Roberts")
    print(julia)

    rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "BB"))
    print(rugby_book)

    novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
    print(novel_book)

    library = Library("Public library")
    library.print_status()

    library.add_new_book(rugby_book)
    library.add_new_book(novel_book)
    library.add_new_member(antoine)
    library.add_new_member(julia)
    library.print_status()

if __name__ == "__main__":
    main()
