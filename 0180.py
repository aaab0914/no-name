class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrower = None

    def borrow(self, borrower_name):
        if self.is_available:
            self.is_available = False
            self.borrower = borrower_name
            return f"Book '{self.title}' borrowed by {borrower_name}"
        return f"Book '{self.title}' is currently unavailable"

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            previous_borrower = self.borrower
            self.borrower = None
            return f"Book '{self.title}' returned by {previous_borrower}"
        return "Book was not borrowed"

    def get_status(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrower}"
        return f"'{self.title}' by {self.author} - {status}"

# Create book objecets
book1 = Book("The Grate Gatsby", "F. Scott Fitzgerald", "978-0743273565")
book2 = Book("To Kill a mockingbird", "Harper Lee", "978-0061120084")

print("=== Test 1: Check initial status ===")
print(book1.get_status())

print("\n=== Test 2: Borrow a book ===")
print(book1.borrow("Alice"))

print("\n=== Test 3: Check status after borrowing ===")
print(book1.get_status())

print("\n=== Test 4: Try to borrow the same book again ===")
print(book1.borrow("Bob"))

print("\n=== Test 5: Return the book ===")
print(book1.return_book())
