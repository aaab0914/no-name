class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.title}' borrowed successfully")
        else:
            print(f"Book '{self.title}' is not available")

    def return_book(self):
        self.is_available = True
        print(f"Book '{self.title}' returned")

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"Book: {self.title} by {self.author}, Pages: {self.pages}, Status: {status}")

book1 = Book("Python Basics", "Dr. Smith", 300)  
book1.display_info()
book1.borrow_book()
book1.return_book()
