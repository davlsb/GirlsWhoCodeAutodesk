# Console Library Management System in Python (GWC TIP Workshop)

## Description
This program serves as an inventory management system for a library, allowing the librarian to keep track of which books are in the library and which ones have been checked out.

## Features
- View a list of each book and its status ("on shelf" or "checked out").
- Add new books to the inventory (default status: "on shelf").
- Toggle the status of each book between "on shelf" and "checked out" via book ID
- Rename the books in the library
- Remove specific "damaged" books from the library via book ID

## Installation
1. Clone the repository to your local machine.
2. Ensure you have [Python](https://www.python.org/downloads/) installed.
3. Navigate to the directory where the program is located.
4. Run the program using the command `python script.py`.

## Usage
1. Upon running the program, follow the command line interface prompts to interact with the inventory management system.
2. Choose from the following options:
    - **Option 1:** Add a new book to the inventory.
    - **Option 2:** Check a book in or out.
    - **Option 3:** Print the status of all library books.
    - **Option 4:** Find the status of a specific book.
    - **Option 5:** Remove a damaged book from the library.
    - **Option 6:** Edit the name of a book in the library.
    - **Option 7:** Quit the program
3. Follow the prompts for each option to perform the desired action.

## Functions
#### Option 1: Add a book
- Description: Allows the user to add a new book to the library inventory.
- Function(s) Used: `add_book(title)`

#### Option 2: Check a book in or out
- Description: Allows the user to toggle the status of a book between "on shelf" and "checked out".
- Function(s) Used: `toggle_status(title)`

#### Option 3: Print all library books' status
- Description: Prints the status of all books in the library.
- Function(s) Used: `print_inventory()`

#### Option 4: Find specific book status
- Description: Allows the user to find and print the status of a specific book.
- Function(s) Used: `book_status(title)`

#### Option 5: Remove damaged book from library
- Description: Allows the user to remove a damaged book from the library inventory.
- Function(s) Used: `remove_book(newtitle, oldtitle)`

#### Option 6: Edit book name in library
- Description: Allows the user to edit the title of a book in the library inventory.
- Function(s) Used: `change_book_name(new_book_name, old_book_name)`


## Acknowledgements
- This program was created as part of Girls Who Code and Autodesk's Technical Interview Prep bootcamp!
