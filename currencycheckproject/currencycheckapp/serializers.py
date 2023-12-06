from rest_framework import serializers
from django.contrib.auth.models import User

from .models import CurrenciesToScrape, Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
                # 'currency_name',
                'currency_shortcut',
                'country',
                'ref_number',
                'purchase_rate',
                'selling_rate',
                'average_exchange_rate',
                'stored_date',
        ]
