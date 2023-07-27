class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        availability = "Available" if self.is_available else "Not Available"
        return f"{self.title} by {self.author} ({availability})"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} (Member ID: {self.member_id})"

    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"{self.name} borrowed '{book.title}' successfully.")
        else:
            print(f"'{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"{self.name} returned '{book.title}' successfully.")
        else:
            print(f"'{book.title}' is not borrowed by {self.name}.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.book_id_counter = 1
        self.member_id_counter = 1

    def add_book(self, title, author):
        book = Book(self.book_id_counter, title, author)
        self.books.append(book)
        self.book_id_counter += 1
        print(f"Book '{title}' by {author} added to the library.")

    def add_member(self, name):
        member = Member(self.member_id_counter, name)
        self.members.append(member)
        self.member_id_counter += 1
        print(f"Member '{name}' added to the library.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        print("Available Books:")
        for book in self.books:
            if book.is_available:
                print(book)

    def display_members(self):
        if not self.members:
            print("No members registered in the library.")
            return

        print("Registered Members:")
        for member in self.members:
            print(member)

    def process_borrowing(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)

        if not member or not book:
            print("Invalid member ID or book ID.")
            return

        member.borrow_book(book)

    def process_returning(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)

        if not member or not book:
            print("Invalid member ID or book ID.")
            return

        member.return_book(book)

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Display Available Books")
        print("4. Display Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            library.add_book(title, author)

        elif choice == "2":
            name = input("Enter the member's name: ")
            library.add_member(name)

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            library.display_members()

        elif choice == "5":
            member_id = int(input("Enter the member ID: "))
            book_id = int(input("Enter the book ID: "))
            library.process_borrowing(member_id, book_id)

        elif choice == "6":
            member_id = int(input("Enter the member ID: "))
            book_id = int(input("Enter the book ID: "))
            library.process_returning(member_id, book_id)

        elif choice == "7":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
