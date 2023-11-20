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

#TODO Add data validation for inserted list of currencies(str)
#TODO Validate if data contains shortcuts matching shortcuts saved in 
# database(list of all known shortcuts to compare). If data cant be parsed 
# to list of string containing shortcuts, return "incorrect_data_exception"
class CurrenciesToScrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrenciesToScrape
        fields = [
            'user',
            'currencies_to_scrape',
        ]
    def validate_currencies_to_scrape(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Currencies must be provided as a list.")

        if not all(isinstance(currency, str) for currency in value):
            raise serializers.ValidationError("Each currency must be a string.")

        return value



# class UserProfileSerializer(serializers.ModelSerializer):
#     currencies = serializers.PrimaryKeyRelatedField(many=True, queryset=Currency.objects.all())

#     class Meta:
#         model = CurrenciesToScrape
#         fields = ['id', 'user', 'currencies']
