
import books as Book
from art import logo, exit_logo
import os


def library():

    filename = "books.txt"
    os.system("cls")
    print(logo)

    while True:
        
        print("1. Add a book")
        print("2. Print all books")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            os.system("cls")
            Book.add_book(filename)
            print(logo)
        elif choice == "2":
            os.system("cls")
            Book.print_books(filename)
        elif choice == "3":
            os.system("cls")
            print(exit_logo)
            break
        else:
            print("\nInvalid choice.\n")


if __name__ == "__main__":
    library()