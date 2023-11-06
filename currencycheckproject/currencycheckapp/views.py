from .webscraper import scrape_website

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Currency
from django.http import JsonResponse

def homepage(request):
    currencies = ["USD", "CHF"]
    display_data = []
    for currency in currencies:
        display_data.extend(scrape_website(currency))
    return JsonResponse(display_data, safe=False)

class CurrencyView(APIView):
    def get(self, request, *args, **kwargs):
        currency_codes = request.GET.get('currency_codes', '')
        currencies = currency_codes.split(',')
        Currency.objects.all().delete()
        Currency.save_data(currencies)
        saved_currencies = Currency.objects.all()
        serialized_currencies = [{'currency_name': currency.currency_name, 'country': currency.country} for currency in saved_currencies]

        return Response(serialized_currencies, status=status.HTTP_200_OK)


 