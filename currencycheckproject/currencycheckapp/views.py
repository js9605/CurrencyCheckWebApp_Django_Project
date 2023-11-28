from .serializers import CurrencySerializer, CurrenciesToScrapeSerializer
from .models import Currency, CurrenciesToScrape
from .services.data_loader import save_currency_data

from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action


class DisplayCurrencyDataViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_currencies = Currency.objects.filter(user=self.request.user)
        return user_currencies
    
    # TODO Clear data after some time
    @action(detail=False, methods=['get'])
    def display(self, request):
        user_currencies = self.get_queryset()

        return render(request, 'exchange_rates.html', {'currencies': user_currencies, 'user': request.user})

    
class LoadCurrencyDataViewSet(viewsets.ModelViewSet):
    queryset = CurrenciesToScrape.objects.all()
    serializer_class = CurrenciesToScrapeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        existing_instance = CurrenciesToScrape.objects.filter(user=self.request.user).first()

        if existing_instance and existing_instance.currencies_to_scrape:
            currencies_to_scrape = existing_instance.currencies_to_scrape.split(',')
            save_currency_data(currencies_to_scrape, self.request.user)
            existing_instance.delete()

        return render(request, 'load_currency_data.html', {'user': request.user})

