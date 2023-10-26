# serializers.py in your Django app
from rest_framework import serializers
from .models import User, Currency, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'currency')

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'currency_name', 'country', 'purchase_rate', 'selling_rate', 'average_exchange_rate', 'value')  

class UserProfileSerializer(serializers.ModelSerializer):
    currencies = CurrencySerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'currencies')