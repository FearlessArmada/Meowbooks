import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def search_libgen(search_term, page_size):
    base_url = "http://libgen.rs/search.php"
    params = {
        "req": search_term,
        "open": "1",
        "res": page_size,
        "view": "simple",
        "phrase": "1",
        "column": "def"
    }
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def truncate_text(text, max_length):
    return text if len(text) <= max_length else text[:max_length-3] + '...'


def parse_table(soup):
    # Find the table in the HTML with the class 'c'
    table = soup.find('table', {'class': 'c'})

    # Find all the rows in the table
    rows = table.find_all('tr')

    data = []  # List to store the data for each row

    # Loop through each row
    for row in rows[1:]:
        # Find all columns in the row
        cols = row.find_all('td')

        # Get the text from the 'ID', 'Title', 'Year', and 'Pages' columns
        id = truncate_text(cols[0].get_text(), 10)
        title = truncate_text(cols[2].get_text(), 30)
        year = truncate_text(cols[4].get_text(), 10)
        pages = truncate_text(cols[5].get_text(), 10)
        size = truncate_text(cols[7].get_text(), 10)
        type = truncate_text(cols[8].get_text(), 10)

        # Add the data to the list
        data.append([id, title, year, pages, size, type])

    # Print the table
    print(tabulate(data, headers=['ID', 'Title', 'Year', 'Pages', 'Size', 'Type'], tablefmt='pipe'))
