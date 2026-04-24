class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []

    def add_book(self, book_name, author):
        # Each book is stored as a dictionary
        book = {
            "book_name": book_name,
            "author": author,
            "available": True
        }
        self.books.append(book)

    def display_available_books(self):
        print("\nAvailable Books:")
        found = False
        for book in self.books:
            if book["available"]:
                print(f"{book['book_name']} by {book['author']}")
                found = True
        if not found:
            print("No books are currently available.")

    def checkout_book(self, book_name):
        for book in self.books:
            if book["book_name"] == book_name:
                if book["available"]:
                    book["available"] = False
                    print(f"You have checked out '{book_name}'.")
                    return
                else:
                    print(f"Sorry, '{book_name}' is already checked out.")
                    return
        print(f"Book '{book_name}' not found.")

    def return_book(self, book_name):
        for book in self.books:
            if book["book_name"] == book_name:
                if not book["available"]:
                    book["available"] = True
                    print(f"You have returned '{book_name}'.")
                    return
                else:
                    print(f"'{book_name}' was not checked out.")
                    return
        print(f"Book '{book_name}' not found.")


# Example usage
library = Library()

library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

library.display_available_books()

library.checkout_book("1984")
library.display_available_books()

library.return_book("1984")
library.display_available_books()