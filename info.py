import requests
import json

def get_book_info(book_id):
    # Define the base URL
    base_url = "http://libgen.rs/json.php"

    # Define the fields to be retrieved
    fields = ['ID', 'Title', 'VolumeInfo', 'Series', 'Periodical', 'Author', 'Year',
              'Edition', 'Publisher', 'City', 'Pages', 'Language', 'Topic', 'Library',
              'Issue', 'Identifier', 'ISSN', 'ASIN', 'UDC', 'LBC', 'DDC', 'LCC', 'Doi',
              'Googlebookid', 'OpenLibraryID', 'Commentary', 'DPI', 'Color', 'Cleaned',
              'Orientation', 'Paginated', 'Scanned', 'Bookmarked', 'Searchable', 'Filesize',
              'Extension', 'MD5', 'CRC32', 'eDonkey', 'AICH', 'SHA1', 'TTH', 'Generic',
              'Visible', 'Locator', 'Local', 'TimeAdded', 'TimeLastModified',
              'Coverurl','identifierwodash', 'tags','pagesinfile', 'descr', 'toc', 'tth', 'sha1', 'aich', 'btih', 'torrent', 'crc32']

    # Define the parameters for the GET request
    params = {
        "ids": book_id,
        "fields": ",".join(fields)
    }

    # Send the GET request
    response = requests.get(base_url, params=params)

    # Check if the response is empty
    if not response.text.strip():
        return None

    try:
        # Parse the JSON response
        data = json.loads(response.text)

        # Return the data for the book
        return data[0] if data else None
    except json.decoder.JSONDecodeError:
        print(f"Error parsing JSON response: {response.text}")
        return None

def print_book_info(book_id):
    # Get the book information
    book_info = get_book_info(book_id)

    # Check if book_info is not None
    if book_info:
        # Iterate over the dictionary and print each key-value pair on a separate line
        for key, value in book_info.items():
            print(f"{key}: {value}")
    else:
        print("No book information found.")