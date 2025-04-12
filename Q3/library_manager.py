import json
import os

# File to store library data
LIBRARY_FILE = "library.json"

def load_library():
    """Load the library from a JSON file."""
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    """Save the library to a JSON file."""
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Add a new book to the library."""
    print("\n📖 Add a New Book")
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower()

    # Validate year input
    while not year.isdigit():
        print("❌ Invalid year. Please enter a valid number.")
        year = input("Enter the publication year: ").strip()

    # Validate read status
    while read_status not in ["yes", "no"]:
        print("❌ Invalid input. Please enter 'yes' or 'no'.")
        read_status = input("Have you read this book? (yes/no): ").strip().lower()

    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status == "yes"
    }

    library.append(book)
    print("✅ Book added successfully!")

def remove_book(library):
    """Remove a book from the library by title."""
    print("\n🗑️ Remove a Book")
    title = input("Enter the title of the book to remove: ").strip()
    found = False

    for book in library[:]:
        if book["title"].lower() == title.lower():
            library.remove(book)
            found = True
            print("✅ Book removed successfully!")
            break

    if not found:
        print("❌ Book not found in the library.")

def search_books(library):
    """Search books by title or author."""
    print("\n🔍 Search for a Book")
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice (1/2): ").strip()

    while choice not in ["1", "2"]:
        print("❌ Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice (1/2): ").strip()

    query = input("Enter your search term: ").strip().lower()
    results = []

    if choice == "1":
        results = [book for book in library if query in book["title"].lower()]
    else:
        results = [book for book in library if query in book["author"].lower()]

    if not results:
        print("❌ No matching books found.")
    else:
        print("\n📚 Matching Books:")
        for i, book in enumerate(results, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_all_books(library):
    """Display all books in the library."""
    print("\n📚 Your Library:")
    if not library:
        print("No books in the library yet.")
        return

    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    """Display library statistics."""
    print("\n📊 Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])

    print(f"Total books: {total_books}")
    if total_books > 0:
        percentage_read = (read_books / total_books) * 100
        print(f"Percentage read: {percentage_read:.1f}%")
    else:
        print("Percentage read: N/A (No books in library)")

def main():
    """Main function to run the library manager."""
    library = load_library()

    while True:
        print("\n📚 Personal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("📁 Library saved to file. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()