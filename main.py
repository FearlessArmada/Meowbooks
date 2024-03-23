from search import search_libgen
from search import parse_table
from info import print_book_info
from get import print_md5_hash


def search(page_size, search_term):
    soup = search_libgen(search_term, page_size)
    return parse_table(soup)


def info(book_id):
    return print_book_info(book_id)


def get(book_id):
    return print_md5_hash(book_id)


def help():
    print("Available commands:")
    print("> search <page_size> <search_term>: Search for books on Libgen with the specified page size and search term.")
    print("  page_size must be 25, 50 or 100. search_term can be any string longer than 2 characters.")
    print("> info <book_id>: Get detailed information about a book with the specified ID.")
    print("> get <book_id>: Get the download link for a book with the specified ID.")
    print("> exit: Exit the program.")


# Map strings to functions
menu = {
    "search": (search, ["page_size", "search_term"]),
    "info": (info, ["book_id"]),
    "get": (get, ["book_id"]),
    "help": (help, []),
    "exit": (exit, []),
}


print("Author: Mia | Copyright 2024 all rights reserved")


# Main loop
while True:
    # Ask the user for input
    user_input = input("$: ")

    # Split the input into the command and its arguments
    command, *args = user_input.split()

    # Check if the command is in the menu
    if command in menu:
        # Get the function and its expected arguments
        func, expected_args = menu[command]

        # Check if the number of arguments matches the expectation
        if len(args) >= len(expected_args):
            # Join all arguments after the first one into a single string
            if len(args) > 1:
                args[1:] = [' '.join(args[1:])]

            # Call the function with the user's arguments
            func(*args)
        else:
            print(f"Invalid number of arguments. Expected at least {len(expected_args)}, got {len(args)}.")
    else:
        print("Invalid command. Please try again or invoke help for further information.")