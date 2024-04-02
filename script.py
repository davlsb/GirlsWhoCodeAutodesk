import time;

# Library is a dictionary with books and status, where the status is a boolean of true or false
library = {}

# Function to print the list of books and their statuses
def print_inventory():
    print("")
    print("Library Inventory:")
    for title, statusArray in library.items():
        print(f"The book {title}")
        for idx, status in enumerate(statusArray):
            print(f'   Book {idx + 1} is {"checked out" if status else "on shelf"}')

# Function to add a new book to the inventory
def add_book(title):
    print("")
    if title not in library:
        library[title] = [False]  # Default status is "on shelf"
        print(f"{title} has been added to the inventory.")
    else:
        library[title].append(False)
        print(f"{title} is already in the inventory, we added another one. There is a total of {len(library[title])} {title} books in our library now.")

# Function to toggle the status of a book between "on shelf" and "checked out", it'll check out the first available
def toggle_status(title):
    if title in library:
        # Add a switch between checking out and checking in - will convert to 2 different functions
        checking = input("Input 1 to check it out, or 2 to check it in: ")
        print("")

        if checking == '1' or checking == "out":
            statusArray = library[title]
            for idx, status in enumerate(statusArray):
                if not status:  # If the book is on shelf
                    statusArray[idx] = True  # Toggle status to checked out
                    print(f"Book {idx + 1} in {title} is now checked out")
                    break  # Stop after toggling the first available book
            else:
                print(f"All books in {title} are already checked out")

        elif checking == '2' or checking == "in":
            idx = input("Please input the ID of the book you want to check in: ") # make sure it's a number
            if idx.isdigit():
                idx = int(idx)
                statusArray = library[title]
                if 1 <= idx <= len(statusArray) and statusArray[idx - 1] == True:
                    library[title][idx - 1] = False  # toggle status to check in
                    print(f"Book {idx} in {title} is now checked back in")
                else:
                    print(f"The book is already checked in")
            else:
                print("You did not input a number.")
        else: 
            print("Invalid choice; Please enter a valid option")
    else:
        print(f"{title} is not in the inventory.")

# Function of specific book status by title
def book_status(title):
    print("")
    if title in library:
        statusArray = library[title]
        print(f"There are {len(statusArray)} {title} book in our library:")
        for idx, status in enumerate(statusArray):
            print(f"   Book {idx + 1} is {'checked out' if status else 'on shelf'}")
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
def remove_book(title, idx):
    print("")
    if title in library:
        statusArray = library[title]
        if 0 <= idx < len(statusArray):  # Check if the index is valid
            del statusArray[idx]
            print(f"Book {idx + 1} in {title} has been damaged and removed from the library.")
        else:
            print(f"Invalid index for {title}.")
    else:
        print(f"{title} is not in the inventory.")

# Main function
def main():

    print("Welcome to our Library :)")

    exit = False

    while(exit is False):
        print("Choose an option:")
        print("1. Add a book")
        print("2. Check a book in or out")
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
            book_name = input("Enter the name of the book to check in or check out: ")
            toggle_status(book_name)
        elif choice == '3':
            print_inventory()
        elif choice == '4':
            book_name = input("Enter the name of the book to check: ")
            book_status(book_name)    
        elif choice == '5':
            book_name = input("Enter the name of the book to remove: ")
            book_id = input("Enter the ID of the book to remove: ")
            if book_id.isdigit():
                book_id = int(book_id) - 1;
                remove_book(book_name, book_id)
            else: 
                print("The ID is not correct")
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

# Tests
add_book("Bone") # Add book Bone
add_book("Rainbow Fish") # Add book Rainbow Fish
add_book("Wild Things") # Add book Wild Things
change_book_name("New Bone", "Bone") # Change book name to New Bone from Bone
add_book("New Bone") # Add another book called New Bone


# Run the main function
if __name__ == "__main__":
    main()