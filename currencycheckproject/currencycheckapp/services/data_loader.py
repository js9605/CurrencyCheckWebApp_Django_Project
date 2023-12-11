from .webscraper import scrape_website
from currencycheckapp.models import Currency, UserCurrency

from django.utils import timezone


def save_currency_data(currencies, user):
    
    currencies_list = update_currency_list(currencies, user)

    for currency in currencies_list:
        
        scraped_data = scrape_website(currency)

        try:
            created_currency = Currency.objects.create(
                currency_shortcut=scraped_data.get('currency_shortcut'),
                country=scraped_data.get('country'),
                ref_number=scraped_data.get('ref_number'),
                purchase_rate=scraped_data.get('purchase_rate'),
                selling_rate=scraped_data.get('selling_rate'),
                average_exchange_rate=scraped_data.get('average_exchange_rate'),
                user=user,
                stored_date=timezone.now(),
            )
            print(f"log: Successfully created currency: {created_currency}")
        except Exception as e:
            print(f"log: Error creating currency: {e}")

def update_currency_list(currencies, user):

    currencies_list = currencies.strip().split(',')
    stored_currencies = []

    for currency in currencies_list:
        existing_currency = UserCurrency.objects.filter(user=user, currency_shortcut=currency).exists()

        if not existing_currency:
            UserCurrency.objects.create(user=user, currency_shortcut=currency)
            print(f"Currency {currency} added for user {user.username}")
        else:
            print(f"Currency {currency} already exists for user {user.username}")

        stored_currencies.extend(UserCurrency.objects.filter(user=user).values_list('currency_shortcut', flat=True))

    # print("log: stored_currencies: ", stored_currencies)

    return stored_currencies
