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
        ]
    
class CurrenciesToScrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrenciesToScrape
        fields = [
            'user',
            'currencies_to_scrape',
        ]



# class UserProfileSerializer(serializers.ModelSerializer):
#     currencies = serializers.PrimaryKeyRelatedField(many=True, queryset=Currency.objects.all())

#     class Meta:
#         model = CurrenciesToScrape
#         fields = ['id', 'user', 'currencies']
