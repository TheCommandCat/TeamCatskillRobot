import requests
from bs4 import BeautifulSoup
import os

# Base URL of the Wiki FLL Israel fandom site
base_url = 'https://fll-israel.fandom.com/he/wiki'

# Start at the main page
url = 'https://fll-israel.fandom.com/he/wiki/%D7%A2%D7%9E%D7%95%D7%93_%D7%A8%D7%90%D7%A9%D7%99'

# Create a directory to save the text files
if not os.path.exists('wiki_pages'):
    os.makedirs('wiki_pages')

while True:
    # Make a request to the current page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the page title
    title = soup.find('h1', class_='page-header__title').text

    # Remove any illegal characters from the title
    title = ''.join(c for c in title if c.isalnum() or c in [' ', '_'])

    # Save the contents of the page to a text file
    with open(f'wiki_pages/{title}.txt', 'w') as f:
        f.write(soup.prettify())

    # Check if there is a "next" button on the page
    next_button = soup.find('a', class_='wds-button wds-is-secondary')
    if next_button:
        # If there is a next button, follow the link
        url = base_url + next_button['href']
    else:
        # If there is no next button, we've reached the last page
        break
