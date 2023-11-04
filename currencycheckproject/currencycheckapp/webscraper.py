import requests
from bs4 import BeautifulSoup


def scrape_website(currency, url='https://www.mbank.pl/serwis-ekonomiczny/kursy-walut/'):
    extracted_currency = extract_currency(html_strip(url), currency)
    return extracted_currency

def html_strip(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    td_elements = soup.find_all('td')
    data = [td.text for td in td_elements]
    
    return data

def extract_currency(html_stripped_data, currency):
    currency_data = {}
    for index, element in enumerate(html_stripped_data):
        if currency in element:
            currency_data['currency_name'] = html_stripped_data[index]
            currency_data['country'] = html_stripped_data[index + 1]
            currency_data['ref_number'] = html_stripped_data[index + 2]
            currency_data['purchase_rate'] = html_stripped_data[index + 3]
            currency_data['selling_rate'] = html_stripped_data[index + 4]
            currency_data['average_exchange_rate'] = html_stripped_data[index + 5]
            break
    return currency_data

# scrape_website()