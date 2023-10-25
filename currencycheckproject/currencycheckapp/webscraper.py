import requests
from bs4 import BeautifulSoup

#TODO scrap only user assigned currencies
def scrape_website(currencies=['USD'], url='https://www.mbank.pl/serwis-ekonomiczny/kursy-walut/'):
    for currency in currencies:
        #TODO save every iteration as separate currency
        extracted_currency = extract_currency(html_strip(url), currency)

    # print(extracted_currency)

    data = []
    data.append(extracted_currency)
    # Example: data['title'] = soup.title.text
    return data

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
            currency_data['spread'] = html_stripped_data[index + 6]
            break
    return currency_data

scrape_website()