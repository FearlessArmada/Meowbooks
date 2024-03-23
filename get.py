import requests
import json

def get_md5_hash(book_id):
    # Define the base URL
    base_url = "http://libgen.rs/json.php"

    # Define the fields to be retrieved
    fields = ['md5']

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

        # Return the MD5 hash for the book
        return data[0]['md5'] if data else None
    except json.decoder.JSONDecodeError:
        print(f"Error parsing JSON response: {response.text}")
        return None

def print_md5_hash(book_id):
    # Get the MD5 hash
    md5_hash = get_md5_hash(book_id)

    # Check if md5_hash is not None
    if md5_hash:
        # Append the MD5 hash to the base URL and print it
        print(f"http://library.lol/main/{md5_hash}")
    else:
        print("No MD5 hash found.")