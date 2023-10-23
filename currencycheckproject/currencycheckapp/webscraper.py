import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Perform scraping tasks using BeautifulSoup
    # Extract data from HTML elements and return the results
    data = {}
    # Example: data['title'] = soup.title.text
    return data
