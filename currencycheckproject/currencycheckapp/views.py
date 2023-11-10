from .serializers import CurrencySerializer
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

    @staticmethod
    def strip_url(url_kwargs):
        currency_codes = url_kwargs.get('currency_codes', '')
        currency_codes = currency_codes.split(',')
        return currency_codes

    def get(self, request, *args, **kwargs):
        currency_codes = self.strip_url(kwargs)
        Currency.objects.all().delete()
        Currency.save_data(currency_codes)
        saved_currencies = Currency.objects.all()
        serializer_data = CurrencySerializer(saved_currencies, many=True).data
        return Response(serializer_data, status=status.HTTP_200_OK)



 