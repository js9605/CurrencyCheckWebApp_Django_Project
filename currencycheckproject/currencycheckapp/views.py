from requests import Response
from rest_framework import viewsets

from .models import User, Currency, UserProfile
from .serializers import UserSerializer, CurrencySerializer, UserProfileSerializer
from .webscraper import scrape_website


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


def UserCurrencyView(request):
    # Assume you have scraped data in scraped_data list
    user = request.user
    scraped_data = scrape_website()

    for data in scraped_data:
        Currency.objects.create(
            user=user,
            currency_name=data['currency_name'],
            country=data['country'],
            ref_number=data['ref_number'],
            purchase_rate=data['purchase_rate'],
            selling_rate=data['selling_rate'],
            average_exchange_rate=data['average_exchange_rate'],
            spread=data['spread'],
            value=data['value']
        )

    return Response({"message": "Scraped data stored successfully"})

# class ScraperView(APIView):
#     def get(self, request):
#         if request.method == 'GET':
#             scraped_data = scrape_website()
#             return Response(scraped_data)