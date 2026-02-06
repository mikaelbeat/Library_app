
import os


def add_book(filename):
    isbn = get_valid_isbn()
    name = get_valid_name()
    writer = get_valid_writer()
    year = get_valid_year()
    
    books = []
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            books = file.readlines()
    except FileNotFoundError:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{isbn},{name},{writer},{year}\n")

    os.system("cls")
    print("\n**** Review book information ****")
    print(f"ISBN:   {isbn}")
    print(f"Name:   {name}")
    print(f"Writer: {writer}")
    print(f"Year:   {year}\n")
    
    while True:
        confirm = input("Do you want to write this book to file? y/n: ").strip().lower()
        
        if confirm == "n":
            os.system("cls")
            print("\nOperation cancelled, returning to main menu.\n")
            return
        elif confirm == "y":
            break
        else:
            print("Invalid input. Please enter y/n.")
    
    books.append(f"{isbn},{name},{writer},{year}\n")
    books.sort(key=sort_by_year)
    
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(books)
    
    os.system("cls")
    print("\nBook added successfully!\n")

def sort_by_year(line):
    return int(line.strip().split(",")[3])


##### Validation functions for user inputs #####   

def get_valid_isbn():
    while True:
        isbn = input("Enter ISBN: ").strip()

        if isbn.isdigit() and 10 <= len(isbn) <= 13 and isbn.startswith("978"):
            return isbn
        else:
            print("Invalid ISBN. Must be 10-13 digits and start with 978.")

def get_valid_name():
    while True:
        name = input("Enter book name: ").strip()

        if len(name) < 1:
            print("Book name cannot be empty.")
        else:
            return name

def get_valid_writer():
    while True:
        name = input("Enter writer: ").strip()

        if len(name) < 1:
            print("Writer name cannot be empty.")
        else:
            return name

def get_valid_year():
    while True:
        year = input("Enter year: ").strip()
        if year.isdigit() and 1900 <= int(year) <= 2026:
            return year
        else:
            print("Please enter a year between 1900 and 2026.")


##### Function to print all books in the library ####

def print_books(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            print("No books found.\n")
            return

        print("\n--- Library collection ---")
        for line in lines:
            isbn, name, writer, year = line.strip().split(",")
            print(f"ISBN: {isbn} | Name: {name} | Writer: {writer} | Year: {year}")
        print()
    except FileNotFoundError:
        print("No book file found yet.\n")