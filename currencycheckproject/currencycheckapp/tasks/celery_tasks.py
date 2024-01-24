from celery import shared_task
from django.core.mail import send_mail

@shared_task
def check_currency_threshold(user_email, currency_shortcut, currency_value, threshold):
    
    print('DEBUG: Enter check_currency_threshold')

    lower_limit = threshold['lower_limit']
    upper_limit = threshold['upper_limit']

    if lower_limit is not None and currency_value['purchase_rate'] > lower_limit:
        subject = 'Currency Threshold Exceeded'
        message = f'The {currency_shortcut} purchase rate ({currency_value["purchase_rate"]}) has exceeded the lower limit ({lower_limit}).'
        from_email = 'tempsurnametempname2@gmail.com'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

    if upper_limit is not None and currency_value['selling_rate'] < upper_limit:
        subject = 'Currency Threshold Exceeded'
        message = f'The {currency_shortcut} selling rate ({currency_value["selling_rate"]}) has exceeded the upper limit ({upper_limit}).'
        from_email = 'tempsurnametempname2@gmail.com'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

    else:
        print("DEBUG: some values are None")

    print("DEBUG: check_currency_threshold task completed.")
