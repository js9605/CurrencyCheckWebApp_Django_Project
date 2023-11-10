from rest_framework import serializers
from .models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
                'currency_name',
                'country',
                'ref_number',
                'purchase_rate',
                'selling_rate',
                'average_exchange_rate',
        ]