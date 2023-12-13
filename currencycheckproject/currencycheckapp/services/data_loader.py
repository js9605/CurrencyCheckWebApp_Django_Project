from .webscraper import scrape_website
from currencycheckapp.models import Currency, UserCurrencies

from django.utils import timezone


def scrape_currency_data(user, currencies = 'USD'):
    
    currencies_list = update_user_currencies_list(currencies, user)

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
            print(f"log: Successfully scraped currency: {created_currency}")
        except Exception as e:
            print(f"log: Error creating currency: {e}")

def update_user_currencies_list(currencies, user):

    currencies_list = currencies.strip().split(',')
    stored_currencies = []

    for currency in currencies_list:
        existing_currency = UserCurrencies.objects.filter(user=user, currency_shortcut=currency).exists()

        if not existing_currency:
            UserCurrencies.objects.create(user=user, currency_shortcut=currency)
            print(f"Currency {currency} added for user {user.username}")
        else:
            print(f"Currency {currency} already exists for user {user.username}")

        stored_currencies.extend(UserCurrencies.objects.filter(user=user).values_list('currency_shortcut', flat=True))

    return stored_currencies
