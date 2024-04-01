import time;

# Library is a dictionary with books and status, where the status is a boolean of true or false
library = {}

# Function to print the list of books and their statuses
def print_inventory():
    print("")
    print("Library Inventory:")
    for title, status in library.items():
        print(f"{title}: {'checked out' if status else 'on shelf'}")

# Function to add a new book to the inventory
def add_book(title):
    print("")
    if title not in library:
        library[title] = False  # Default status is "on shelf"
        print(f"{title} has been added to the inventory.")
    else:
        print(f"{title} is already in the inventory.")

# Function to toggle the status of a book between "on shelf" and "checked out"
def toggle_status(title):
    print("")
    if title in library:
        library[title] = not library[title]
        print(f"{title} is now {'checked out' if library[title] else 'on shelf'}")
    else:
        print(f"{title} is not in the inventory.")

# Function of specific book status by title
def book_status(title):
    print("")
    if title in library:
        print(f"{title} is {'checked out' if library[title] else 'on shelf'}")
    else:
        print(f"{title} is not in the inventory.")

# Function to change book name
def change_book_name(newtitle, oldtitle):
    print("")
    if oldtitle in library and newtitle not in library:
        library[newtitle] = library.pop(oldtitle)
        print(f"{oldtitle} has been changed to {newtitle}")
    else:
        print(f"{oldtitle} is not in the inventory or {newtitle} is already taken.")

# Function to remove a specific book from library
def remove_book(title):
    print("")
    if title in library:
        del library[title]
        print(f"{title} has been damaged and removed from library.")
    else:
        print(f"{title} is not in the inventory.")

# If i add a multiple, value should have total and checked out. if total - checked out > 0 then it can be checked out

# Main function
def main():

    print("Welcome to the Library Management System!")

    # Add to only be able to add a book on the first interaction? / if library is empty?

    exit = False

    while(exit is False):
        print("Choose an option:")
        print("1. Add a book")
        print("2. Change status of a book")
        print("3. Print all library books' status")
        print("4. Find specific book status")
        print("5. Remove damaged book from library")
        print("6. Edit book name in library")
        print("7. Exit Library")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_name = input("Enter the name of the book to add: ")
            add_book(book_name)
        elif choice == '2':
            book_name = input("Enter the name of the book to toggle: ")
            toggle_status(book_name)
        elif choice == '3':
            print_inventory()
        elif choice == '4':
            book_name = input("Enter the name of the book to check: ")
            book_status(book_name)    
        elif choice == '5':
            book_name = input("Enter the name of the book to remove: ")
            remove_book(book_name)
        elif choice == '6':
            old_book_name = input("Enter the old name of the book to change: ")
            new_book_name = input("Enter the new name of the book to change: ")
            change_book_name(new_book_name, old_book_name)
        elif choice == '7':
            print("")
            print("Thank you for coming to the library, bye bye :)")
            exit = True
        else:
            print("Invalid choice. Please enter a valid option.")
        time.sleep(2) 
        print("");

# Run the main function
if __name__ == "__main__":
    main()