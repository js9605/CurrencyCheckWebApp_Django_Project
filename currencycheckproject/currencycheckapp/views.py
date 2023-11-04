from .webscraper import scrape_website
from django.http import JsonResponse

def homepage(request, *args, **kwargs):
    currencies = ["USD", "CHF"]
    display_data = []
    for currency in currencies:
        display_data.append(scrape_website(currency))
    return JsonResponse(display_data, safe=False)