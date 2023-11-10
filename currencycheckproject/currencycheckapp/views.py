from .webscraper import scrape_website
from .models import Currency

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def homepage(request):
    if request.method != "GET":
        return Response({"detail": "GET not allowed"}, status=405)
    currencies = ["USD", "CHF"]
    display_data = {"currencies": {}}

    for currency_code in currencies:
        currency_data = scrape_website(currency_code)
        display_data["currencies"][currency_code] = currency_data
    return Response(display_data)

class CurrencyView(APIView):
    def get(self, request, *args, **kwargs):
        currency_codes = kwargs.get('currency_codes', '')
        currencies = currency_codes.split(',')
        Currency.objects.all().delete()
        Currency.save_data(currencies)
        saved_currencies = Currency.objects.all()
        serialized_currencies = [{'currency_name': currency.currency_name,
                                   'country': currency.country, 'average_exchange_rate': currency.average_exchange_rate
                                   } for currency in saved_currencies]

        return Response(serialized_currencies, status=status.HTTP_200_OK)


 