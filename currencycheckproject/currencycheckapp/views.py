from django.forms import model_to_dict
from .webscraper import scrape_website
from django.http import JsonResponse
from .models import Currency

def homepage(request, *args, **kwargs):
    currencies = ["USD", "CHF"]
    display_data = []
    for currency in currencies:
        display_data.extend(scrape_website(currency))
    return JsonResponse(display_data, safe=False)


def currency_view(request):
    Currency.objects.all().delete()
    Currency.save_data()
    currencies = Currency.objects.all()
    serialized_currencies = [model_to_dict(currency) for currency in currencies]
    return JsonResponse(serialized_currencies, safe=False)
 