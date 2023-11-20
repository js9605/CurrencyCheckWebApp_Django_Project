from .serializers import CurrencySerializer, CurrenciesToScrapeSerializer
from .models import Currency, CurrenciesToScrape

from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]

    def custom_action(self, request):
        # logic here
        return Response({"message": "Custom action executed"}, status=200)
    
class CurrenciesToScrapeViewSet(viewsets.ModelViewSet):
    queryset = CurrenciesToScrape.objects.all()
    print(type(queryset))
    serializer_class = CurrenciesToScrapeSerializer#.validate_currencies_to_scrape()
    permission_classes = [permissions.IsAuthenticated]

