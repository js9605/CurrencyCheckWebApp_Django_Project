import requests
from bs4 import BeautifulSoup


DEFAULT_URL = 'https://www.mbank.pl/serwis-ekonomiczny/kursy-walut/'

def scrape_website(currency, url=DEFAULT_URL):
    extracted_currency = extract_currency(get_html_elements(url), currency)
    return extracted_currency

def get_html_elements(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    td_elements = soup.find_all('td')
    data = [td.text for td in td_elements]
    
    return data


def extract_currency(html_stripped_data, currency):
    currency_data = {}
    for index, element in enumerate(html_stripped_data):
        if currency == element:
            try:
                currency_data['currency_shortcut'] = html_stripped_data[index]
                currency_data['country'] = html_stripped_data[index + 1]
                currency_data['ref_number'] = int(html_stripped_data[index + 2])
                currency_data['purchase_rate'] = html_stripped_data[index + 3]
                currency_data['selling_rate'] = html_stripped_data[index + 4]
                currency_data['average_exchange_rate'] = html_stripped_data[index + 5]
            except ValueError as e:
                print(f"log: ValueError - You're scraping: {currency}, Error: {e}")
            break

    return currency_data