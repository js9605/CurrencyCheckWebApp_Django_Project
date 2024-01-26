from currencycheckapp.tasks.celery_tasks import check_currency_threshold
from currencycheckapp.models import Currency, UserCurrencies

from celery import shared_task


# Using this in celery.py for scheduling
@shared_task
def fetch_currency_values_and_notify():
    print("DEBUG: Entered fetch_currency_values_and_notify")

    user_currencies_list = UserCurrencies.objects.all()

    for user_currency in user_currencies_list:
        
        user = user_currency.user
        currency_shortcut = user_currency.currency_shortcut
        user_email = user_currency.user_email

        currency_rates = get_currency_value(user, currency_shortcut)
        threshold = get_threshold(user, currency_shortcut)

        print(f"DEBUG: arguments for check_currency_threshold: {currency_shortcut, user_email, currency_rates, threshold}")

        # check_currency_threshold.apply_async(args=(user_email, currency_shortcut, currency_rates, threshold))
        # check_currency_threshold.delay(user_email, currency_shortcut, currency_rates, threshold)
        check_currency_threshold.delay(user_email=user_email, currency_shortcut=currency_shortcut, currency_value=currency_rates, threshold=threshold)

@shared_task
def get_currency_value(user, currency_shortcut) -> dict:
    try:
        currency = Currency.objects.get(user=user, currency_shortcut=currency_shortcut)
        currency_rates = {'purchase_rate': currency.purchase_rate, 'selling_rate': currency.selling_rate}
        return currency_rates
    
    except Currency.DoesNotExist:
        print("DEBUG: Currency.DoesNotExist in notification_handler.get_currency_value")
        return None

@shared_task
def get_threshold(user, currency_shortcut) -> dict:
    try:
        user_currency = UserCurrencies.objects.filter(user=user, currency_shortcut=currency_shortcut).order_by('-id').first()
        threshold = {'upper_limit': user_currency.upper_limit, 'lower_limit': user_currency.lower_limit}
        print(f'DEBUG: in func(get_threshold) for {user_currency} upper_limit: {threshold["upper_limit"]} lower_limit: {threshold["lower_limit"]}')
        return threshold
    
    except Exception as e:
        print(f"DEBUG: An exception occurred: {e}")
        return {'upper_limit': None, 'lower_limit': None}
