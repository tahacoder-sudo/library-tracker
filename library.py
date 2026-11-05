# library.py
# A simple command-line library tracker.
books = {}  # title -> {"author": str, "available": bool}

def show_menu():
    print("\n=== Library Tracker ===")
    print("1. Add book")
    print("2. List books")
    print("3. Borrow book")
    print("0. Exit")

def add_book():
    title = input("Title: ")
    if title in books:
        print(f'"{title}" is already in the library.')
        return
    author = input("Author: ")
    books[title] = {"author": author, "available": True}
    print(f'Added "{title}".')

def list_books():
    if not books:
        print("No books in the library.")
    else:
        for title, info in books.items():
            status = "Available" if info["available"] else "Borrowed"
            print(f'{title} by {info["author"]}\n{status}')

def borrow_book():
    title = input("Title: ")
    if title not in books:
        print(f'No book titled "{title}".')
    elif not books[title]["available"]:
        print(f'"{title}" is already borrowed.')
    else:
        books[title]["available"] = False
        print(f'You borrowed "{title}".')

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            borrow_book()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()