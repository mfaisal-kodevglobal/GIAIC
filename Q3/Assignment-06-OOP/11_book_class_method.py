class Book:
    total_books = 0  # Class variable to track total books
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Call class method when new book is created
    
    @classmethod
    def increment_book_count(cls):
        """Class method to increment the total book count"""
        cls.total_books += 1
    
    @classmethod
    def get_total_books(cls):
        """Class method to get the current total book count"""
        return cls.total_books

# Create some books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Check the total
print(f"Total books in library: {Book.get_total_books()}")  # Output: 2

# Create another book
book3 = Book("1984", "George Orwell")
print(f"Total books after adding another: {Book.get_total_books()}")  # Output: 3