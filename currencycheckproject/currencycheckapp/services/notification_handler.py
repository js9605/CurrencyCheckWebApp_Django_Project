from currencycheckapp.tasks.celery_tasks import check_currency_threshold


# Using this in celery.py for scheduling
def fetch_currency_values_and_notify(user_email):

    #TODO Fetch currency values (replace with  logic)
    currency_value = get_currency_value()

    threshold = get_threshold()


    #TODO Call Celery task to check threshold and send email
    check_currency_threshold.delay(user_email, currency_value, threshold)