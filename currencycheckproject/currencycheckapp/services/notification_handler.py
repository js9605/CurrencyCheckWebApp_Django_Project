from currencycheckapp.tasks.celery_tasks import check_currency_threshold
from currencycheckproject.currencycheckapp.models import Currency, UserCurrencies


# Using this in celery.py for scheduling
def fetch_currency_values_and_notify():

    currency_value = get_currency_value()
    threshold = get_threshold()
    user_email = get_user_email()

    check_currency_threshold.delay(user_email, currency_value, threshold)

# TODO How pass these args here?
def get_currency_value(user, currency_shortcut, criterion='purchase_rate'):
    try:
        currency = Currency.objects.get(user=user, currency_shortcut=currency_shortcut)
        return getattr(currency, criterion)
    except Currency.DoesNotExist:
        print("log: Currency.DoesNotExist in notification_handler.get_currency_value")
        return None

def get_threshold(user, currency_shortcut):
    try:
        user_currency = UserCurrencies.objects.get(user=user, currency_shortcut=currency_shortcut)
        threshold = {'upper_limit': user_currency.upper_limit, 'lower_limit': user_currency.lower_limit}
        return threshold
    
    except UserCurrencies.DoesNotExist:
        print("log: UserCurrencies.DoesNotExist in notification_handler.get_threshold")
        return None

def get_user_email():
    #TODO Implement the logic to get the user's email address
    # For example, if you have a User model with an email field, you can retrieve it as follows:
    # return User.objects.get(username='your_username').email
    pass


#TODO Example usage

# # Assuming you have a logged-in user (replace 'logged_user' with your actual user variable)
# logged_user = request.user  # or however you retrieve the logged-in user in your view/controller

# # Get the purchase rate for the currency with shortcut 'USD' for the logged-in user
# purchase_rate_usd = get_currency_value(logged_user, 'USD', criterion='purchase_rate')
