# Meowbooks

Books are a human right and knowledge should not be locked behind paywalls. I aim to make accessing books and information easier for everyone. I do not encourage theft, piracy is not theft.

## Features

- Query books with a search term.
- Retrieve book information based on book ID.
- Retrieve download link for IPFS and Tor based mirrors.


## Usage

1. `search <page_size> <search_term>`: Search for books on Libgen with the specified page size and search term. The `page_size` must be 25, 50, or 100. The `search_term` can be any string longer than 2 characters.

2. `info <book_id>`: Get detailed information about a book with the specified ID. The information includes the book's title, author, publisher, year, pages, language, size, and format.

3. `get <book_id>`: Get the download link for a book with the specified ID.


## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.