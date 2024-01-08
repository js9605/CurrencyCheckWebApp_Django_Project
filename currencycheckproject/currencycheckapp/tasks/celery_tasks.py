from celery import shared_task
from django.core.mail import send_mail

@shared_task
def check_currency_threshold(user_email, currency_shortcut, currency_value, threshold):
    
    print('log: currency values and threshold limits')
    print(currency_value['purchase_rate'], threshold['upper_limit'])
    print(currency_value['selling_rate'], threshold['lower_limit'])

    if currency_value['purchase_rate'] > threshold['upper_limit'] or currency_value['selling_rate'] < threshold['lower_limit']: 
        subject = 'Currency Threshold Exceeded'
        message = f'The {currency_shortcut} value ({currency_value}) has exceeded the threshold ({threshold}).'
        from_email = 'your@example.com'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


    print("Currency Threshold Exceeded task completed.")