from .webscraper import scrape_website
from currencycheckapp.models import Currency


def save_currency_data(currencies, user):
    for currency in currencies:
        scraped_data = scrape_website(currency)

        try:
            created_currency = Currency.objects.create(
                currency_shortcut=scraped_data.get('currency_shortcut'),
                country=scraped_data.get('country'),
                ref_number=scraped_data.get('ref_number'),
                purchase_rate=scraped_data.get('purchase_rate'),
                selling_rate=scraped_data.get('selling_rate'),
                average_exchange_rate=scraped_data.get('average_exchange_rate'),
                user=user
            )
            print(f"Successfully created currency: {created_currency}")
        except Exception as e:
            print(f"Error creating currency: {e}")
