class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'"{self.title}" has been borrowed.')
        else:
            print(f'"{self.title}" is already borrowed.')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" was not borrowed.')


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print("Book is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print("This book was not borrowed by the patron.")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")

        book = Book(title, author, isbn)
        self.books.append(book)

        print("Book added successfully!")

    def register_patron(self):
        name = input("Enter patron name: ")
        patron_id = input("Enter patron ID: ")

        patron = Patron(name, patron_id)
        self.patrons.append(patron)

        print("Patron registered successfully!")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nBooks in Library:")
            for book in self.books:
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")



library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Display Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.register_patron()

    elif choice == "3":
        library.display_books()

    elif choice == "4":
        if library.books and library.patrons:
            book = library.books[0]
            patron = library.patrons[0]
            patron.borrow_book(book)
        else:
            print("Please add a book and register a patron first.")

    elif choice == "5":
        if library.books and library.patrons:
            book = library.books[0]
            patron = library.patrons[0]
            patron.return_book(book)
        else:
            print("No borrowed books found.")

    elif choice == "6":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice.")