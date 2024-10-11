import mysql.connector
db_name = "new_schema"
user = "root"
password = "Z3bEnn1%402024"
host = "localhost"

class LibraryManagement:

    import mysql.connector

db_name = "new_schema"
user = "root"
password = "Z3bEnn1%402024"
host = "localhost"

class LibraryManagement:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def get_bookOperations(self):
        while True:
            menu = input("Book Operations:\n1. Add a book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Quit to main menu\n")
            if menu == "1":
                book_title = input("Which book to add? ")
                self.cursor.execute("INSERT INTO books (title) VALUES (%s)", (book_title,))
                self.connection.commit()
                print(f"Book '{book_title}' added.")
            elif menu == "2":
                book_to_borrow = input("Which book to borrow? ")
                self.cursor.execute("DELETE FROM books WHERE title = %s", (book_to_borrow,))
                if self.cursor.rowcount > 0:
                    self.connection.commit()
                    print(f"Book '{book_to_borrow}' borrowed.")
                else:
                    print("Book not found.")
            elif menu == "3":
                book_to_return = input("Return which book? ")
                self.cursor.execute("INSERT INTO books (title) VALUES (%s)", (book_to_return,))
                self.connection.commit()
                print(f"Book '{book_to_return}' returned.")
            elif menu == "4":
                book_search = input("What book are you looking for? ")
                self.cursor.execute("SELECT * FROM books WHERE title = %s", (book_search,))
                result = self.cursor.fetchone()
                if result:
                    print(f"Book found: {result}")
                else:
                    print("Book not found.")
            elif menu == "5":
                self.cursor.execute("SELECT * FROM books")
                books = self.cursor.fetchall()
                print("All books:")
                for book in books:
                    print(book)
            elif menu == "6":
                break
            else:
                print("Invalid selection.")

    def get_userOperations(self):
        while True:
            menu = input("User Operations\n1. Add a new user\n2. View user details\n3. Display all users\n4. Quit to main menu\n")
            if menu == "1":
                username = input("Enter username: ")
                self.cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
                self.connection.commit()
                print(f"User '{username}' added.")
            elif menu == "2":
                selectUser = input("Which username? ")
                self.cursor.execute("SELECT * FROM users WHERE username = %s", (selectUser,))
                user = self.cursor.fetchone()
                if user:
                    print(f"User found: {user}")
                else:
                    print("User not found.")
            elif menu == "3":
                self.cursor.execute("SELECT * FROM users")
                users = self.cursor.fetchall()
                print("All users:")
                for user in users:
                    print(user)
            elif menu == "4":
                break
            else:
                print("Invalid selection.")

    def get_authorOperations(self):
        while True:
            menu = input("Author Operations\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Quit to main menu\n")
            if menu == "1":
                author_name = input("Enter author name: ")
                self.cursor.execute("INSERT INTO authors (name) VALUES (%s)", (author_name,))
                self.connection.commit()
                print(f"Author '{author_name}' added.")
            elif menu == "2":
                author = input("Which author? ")
                self.cursor.execute("SELECT * FROM authors WHERE name = %s", (author,))
                author_details = self.cursor.fetchone()
                if author_details:
                    print(f"Author found: {author_details}")
                else:
                    print("Author not found.")
            elif menu == "3":
                self.cursor.execute("SELECT * FROM authors")
                authors = self.cursor.fetchall()
                print("All authors:")
                for author in authors:
                    print(author)
            elif menu == "4":
                break
            else:
                print("Invalid selection.")

library = LibraryManagement()

def main():
    try:
        while True:
            menu = input("Welcome to the Library Management System!\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit\n")
            if menu == "1":
                library.get_bookOperations()
            elif menu == "2":
                library.get_userOperations()
            elif menu == "3":
                library.get_authorOperations()
            elif menu == "4":
                break
            else:
                print("Invalid selection.")
    finally:
        library.close_connection()

main()
