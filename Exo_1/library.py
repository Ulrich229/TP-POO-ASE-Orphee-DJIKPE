class Person:
    """Class defining a person"""
    def __init__(self, last_name: str, first_name: str,) -> None:
        self.first_name = first_name.capitalize()
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
    
    def __repr__(self) -> str:
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
        if book  not in self._books:
            raise LibraryError('Book not in the library')
        elif book in self._borrowed_books.keys():
            raise LibraryError("Book borrowed")
        else:
            return True
    
    def borrow_book(self,book: Book, person: Person) -> None:
        if(person not in self._members):
            raise LibraryError(f"{person} is not a member of the library")
        else:
            try:
                if self.is_book_available(book):
                    self._borrowed_books[book] = person 

            except LibraryError as error:
                if str(error) == "Book borrowed":
                    raise LibraryError(f"{book} is already borrowed by {self._borrowed_books[book]}")
                else:
                    raise LibraryError(f"{book} doesn't exist in the library")


            

    def return_book(self,book: Book) -> None:
        if (book not in self._borrowed_books.keys()):
            raise LibraryError(f"{book} is not part of the borrowed books")
        else:
            self._borrowed_books.pop(book)


    def add_new_member(self, person:Person)-> None:
        self._members.add(person)
    
    def add_new_book(self, book:Book)->None:
        self._books.append(book)
    
    def print_status(self):
        available_books = []
        for book in self._books:
            try:
                if self.is_book_available(book):
                    available_books.append(book)
            except:
                pass
        

        print(f"{self.name} status:")
        print(f"Books catalogue: {self._books}")
        print(f"Members: {self._members}")
        print(f"Available books: {available_books}")
        print(f"Borrowed books: {self._borrowed_books}")
        print("-----")


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

    print(f"Is {rugby_book} available? {library.is_book_available(rugby_book)}")
    library.borrow_book(rugby_book, antoine)
    library.print_status()

    try:
        library.borrow_book(rugby_book, julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(Book("Roméo et Juliette", Person("William", "Shakespeare")), julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(novel_book, Person("Simone", "Veil"))
    except LibraryError as error:
        print(error)

    try:
        library.return_book(novel_book)
    except LibraryError as error:
        print(error)

    library.return_book(rugby_book)
    library.borrow_book(novel_book, julia)
    library.print_status()

    library.borrow_book(rugby_book, julia)
    library.print_status()

if __name__ == "__main__":
    main()
