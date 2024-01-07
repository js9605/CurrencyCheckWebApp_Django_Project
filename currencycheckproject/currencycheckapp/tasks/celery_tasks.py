from celery import shared_task
from django.core.mail import send_mail

@shared_task
def check_currency_threshold(user_email, currency_shortcut, currency_value, threshold):
    
    if currency_value > threshold: #TODO add "or" for lower and upper limit
        subject = 'Currency Threshold Exceeded'
        message = f'The {currency_shortcut} value ({currency_value}) has exceeded the threshold ({threshold}).'
        from_email = 'your@example.com'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


    print("Currency Threshold Exceeded task completed.")