from .serializers import CurrencySerializer, CurrenciesToScrapeSerializer
from .models import Currency, CurrenciesToScrape
from .services.data_loader import save_currency_data

from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action


class DisplayCurrencyDataViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def display_data(self, request):
        user_currencies = Currency.objects.filter(user=request.user).all()
        return Response({user_currencies}, status=200)
    
class LoadCurrencyDataViewSet(viewsets.ModelViewSet):
    queryset = CurrenciesToScrape.objects.all()
    serializer_class = CurrenciesToScrapeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        existing_instance = self.queryset.filter(user=self.request.user).all()
        if existing_instance:
            existing_instance.delete()
            save_currency_data(list(existing_instance)) #TODO list(existing_instance) ~ Empty list

        return super().create(request, *args, **kwargs)