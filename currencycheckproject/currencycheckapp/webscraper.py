import requests
from bs4 import BeautifulSoup


def scrape_website(currency, url='https://www.mbank.pl/serwis-ekonomiczny/kursy-walut/'):
    extracted_currency = extract_currency(html_strip(url), currency)
    print("HERE: ", extracted_currency)
    return extracted_currency

def html_strip(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    td_elements = soup.find_all('td')
    data = [td.text for td in td_elements]
    
    return data


#TODO If i add currency_name as first scraped data starts with USD and ref_number is at purchase_rate
# If I comment out currency_name scraped data starts with DOLAR and ref_number is at country
def extract_currency(html_stripped_data, currency):
    currency_data = {}
    print("html_stripped_data: ", html_stripped_data)
    for index, element in enumerate(html_stripped_data):
        if currency in element:
            # currency_data['currency_name'] = html_stripped_data[index]
            currency_data['currency_shortcut'] = html_stripped_data[index]
            currency_data['country'] = html_stripped_data[index + 1]
            currency_data['ref_number'] = html_stripped_data[index + 2]
            currency_data['purchase_rate'] = html_stripped_data[index + 3]
            currency_data['selling_rate'] = html_stripped_data[index + 4]
            currency_data['average_exchange_rate'] = html_stripped_data[index + 5]
            break

    return currency_data

# scrape_website()