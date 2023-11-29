from .serializers import CurrencySerializer, CurrenciesToScrapeSerializer
from .models import Currency, CurrenciesToScrape
from .services.data_loader import save_currency_data

from django.utils import timezone
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView


class DisplayCurrencyDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_currencies = Currency.objects.filter(user=self.request.user)
        return user_currencies
    
    @action(detail=False, methods=['get'])
    def display(self, request):
        cutoff_date = timezone.now() - timezone.timedelta(days=1)
        Currency.objects.filter(user=request.user, stored_date__lt=cutoff_date).delete()

        user_currencies = self.get_queryset()

        return render(request, 'exchange_rates.html', {'currencies': user_currencies, 'user': request.user})


class LoadCurrencyDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print("Enter create method")
        currencies_to_scrape = request.data.get('currencies_to_scrape', '').strip()

        if currencies_to_scrape:
            created = CurrenciesToScrape.objects.update_or_create(
                user=request.user,
                defaults={'currencies_to_scrape': currencies_to_scrape}
            )

            if created:
                save_currency_data(currencies_to_scrape, request.user)
                return render(request, 'load_currency_data.html', {'user': request.user})
            else:
                print("currencies_to_scrape not created")
                return render(request, 'load_currency_data.html', {'user': request.user})
        else:
            return Response({'error': 'Currencies cannot be empty.'}, status=400)
