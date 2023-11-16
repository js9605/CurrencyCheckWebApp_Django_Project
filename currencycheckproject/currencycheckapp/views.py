from .serializers import CurrencySerializer, UserSerializer, UserRegistrationSerializer
from .webscraper import scrape_website
from .models import Currency, UserProfile

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


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
    

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


@login_required
@api_view(['GET','POST'])
def set_currencies_to_scrape(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    print("User created: ", created)

    if request.method == 'POST':
        currencies = request.POST.get('currencies', '')
        user_profile.currencies_to_scrape = currencies
        user_profile.save()

    saved_currencies = user_profile.currencies_to_scrape if user_profile.currencies_to_scrape else "No currencies saved."

    Currency.objects.all().delete()
    Currency.save_data(saved_currencies)

    saved_currencies_data = Currency.objects.all()
    serializer_data = CurrencySerializer(saved_currencies_data, many=True).data

    return render(request, 'set_currencies_to_scrape.html', {'saved_currencies': saved_currencies})


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




 